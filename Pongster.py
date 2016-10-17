from graphics import *
import random
import math
#from button import *

class Pongster:
    def __init__(self, w):
        self.w = w
        self.menuElements = []
        self._initMenu()
        self.balls = []
        self.addRandomBall()
        self.paddles = []
        self.paddlesai = [False, False]
        self.screenDrawn = None
        self.score = [0, 0]
        self.scoreText = Text(Point(w.getWidth()/2, w.getHeight()/8), "0 - 0")
        self.mfcount = 0
        self.mfcountText = Text(Point(w.getWidth()/2, w.getHeight()/8*7), "m'otherfucker: 0")
        self.paddles.append(Paddle(w.getWidth()/8, 100, w))
        self.paddles.append(Paddle(w.getWidth()/8*7, 100, w))
    
    def drawMenu(self):
        if self.screenDrawn != "Menu":
            self._undrawScreen()
            for element in self.menuElements:
                element.draw(self.w)
            self.screenDrawn = "Menu"
            
    def drawGame(self):
        if self.screenDrawn != "Game":
            self._undrawScreen()
            for ball in self.balls:
                ball.draw(self.w)
            for paddle in self.paddles:
                paddle.draw(self.w)
            self.scoreText.draw(self.w)
            self.mfcountText.draw(self.w)
            self.screenDrawn = "Game"
            
    def _undrawScreen(self):
        if self.screenDrawn == "Menu":
            for element in self.menuElements:
                element.undraw()
            self.screenDrawn = None
        elif self.screenDrawn == "Game":
            for ball in self.balls:
                ball.undraw()
            for paddle in self.paddles:
                paddle.undraw()
            self.screenDrawn = None
        #elif self.screenDrawn == "Settings":
            
    def _initMenu(self):
        self.menuElements.append(Rectangle(Point(100, 100), Point(200, 200)))
        self.menuElements.append(Text(Point(150, 150), "Play!"))
        self.menuElements.append(Rectangle(Point(100, 250), Point(200, 350)))
        self.menuElements.append(Text(Point(150, 300), "Settings!"))
        self.menuElements.append(Rectangle(Point(100, 400), Point(200, 500)))
        self.menuElements.append(Text(Point(150, 450), "Quit!"))

    def handleClick(self, p):
        '''
        for i in range(3):
            if p.getY() >= 100+150*i and p.getY() <= 200+150*i and p.getX() >= 100 and p.getX() <= 200:
                if i == 0:
                    self.drawGame()
        '''
        
    def move(self):
        for ball in self.balls:
            self._moveBall(ball, ball.xv, ball.yv)
            '''
            x = ball.c.getCenter().getX()
            y = ball.c.getCenter().getY()
            width = self.w.getWidth()
            height = self.w.getHeight()
            r = ball.c.getRadius()

            paddle1 = self.paddles[0].getSize()       
            if x + ball.xv >= width - r:
                ball.xv = -ball.xv
   
            if x + ball.xv <= 0 + r:
                ball.xv = -ball.xv

            if y + ball.yv >= height - r:
                ball.yv = -ball.yv
            
            if y + ball.yv <= 0 + r:
                ball.yv = -ball.yv
                
            for paddle in self.paddles:
                p = paddle.getSize()
                if ((x >= p.getP2().getX()+r and x + ball.xv <= p.getP2().getX()+r) or (x <= p.getP1().getX()-r and x + ball.xv >= p.getP1().getX()-r)):
                    if (y + ball.yv + r >= p.getP1().getY() and y + ball.yv - r <= p.getP2().getY()):
                        ball.xv = -ball.xv*1.01
                        print ball.xv
                        if math.fabs(p.getCenter().getY()- y) > (p.getP2().getY() - p.getP1().getY())/2:
                            if y > p.getCenter().getY():
                                ball.yv += 7
                            else:
                                ball.yv -= 7
                        else:
                            ball.yv += (y-p.getCenter().getY())/50
                #TODO: maek stronk in Y DIRECTION pls...
            ball.c.move(ball.xv, ball.yv)
            '''
    def _moveBall(self, ball, xv, yv):
        x = ball.c.getCenter().getX()
        y = ball.c.getCenter().getY()
        width = self.w.getWidth()
        height = self.w.getHeight()
        r = ball.c.getRadius()
        dx = xv
        dy = yv
        bounceX = False
        bounceY = False
        goal = False
        for paddle in self.paddles:
            p = paddle.getSize()
            if y + ball.yv + r >= p.getP1().getY() and y + ball.yv - r <= p.getP2().getY():
                if x >= p.getP2().getX()+r and x + ball.xv <= p.getP2().getX()+r:
                    dx = p.getP2().getX()+r-x
                    bounceX = True
                if x <= p.getP1().getX()-r and x + ball.xv >= p.getP1().getX()-r and not bounceX:
                    dx = p.getP1().getX()-r-x
                    bounceX = True
                if bounceX:
                    if math.fabs(p.getCenter().getY()- y) > (p.getP2().getY() - p.getP1().getY())/2:
                        self.mfcount += 1
                        self.updateText()
                        if y > p.getCenter().getY():
                            ball.yv += 3
                        else:
                            ball.yv -= 3
                    else:
                        ball.yv += (y-p.getCenter().getY())/50

        if not bounceX:
            if x + xv >= width - r:
                goal = True
                bounceX = True
                self.score[0] += 1
                self.updateText()
                ball.undraw()
                self.balls.remove(ball)
            elif x + xv <= 0 + r:
                goal = True
                bounceX = True
                self.score[1] += 1
                self.updateText()
                ball.undraw()
                self.balls.remove(ball)
        if not bounceY:
            if y + yv >= height - r:
                dy = height-r-y
                ball.yv = -ball.yv
            elif y + yv <= 0 + r:
                dy = r-y
                ball.yv = -ball.yv
        if bounceX:
            if math.fabs(ball.xv) < 100:
                ball.xv = ball.xv*1.05
            ball.xv = -ball.xv
        restx = xv-dx
        resty = yv-dy
        ball.c.move(dx, dy)
        if not goal:
            if restx != 0 and resty != 0:
                self._moveBall(ball, -restx, -resty)
        else:
            if len(self.balls) == 0:
                self.reset()

    def reset(self):
        for ball in self.balls:
            self.balls.remove(ball)
        self.addRandomBall()
        self.balls[0].draw(self.w)
        for paddle in self.paddles:
            dy = self.w.getHeight()/2 - paddle.getSize().getCenter().getY()
            paddle.movePaddle(dy)
        time.sleep(1)
        self.w.getKey()
    
    def updateText(self):
        self.mfcountText.setText("m'otherfucker: " + str(self.mfcount))
        self.scoreText.setText(str(self.score[0]) + " - " + str(self.score[1]))
    
    def addBall(self, B):
        self.balls.append(B)

    def addRandomBall(self):
        xv = random.uniform(1, 2)
        yv = random.uniform(1, 2)
        
        if random.randint(0, 1) == 1:
            xv = -xv
        if random.randint(0, 1) == 1:
            yv = -yv
        self.addBall(Ball(Point(self.w.getWidth()/2, self.w.getHeight()/2), xv, yv))
    def movePaddle(self, paddleN, y):
        
        paddle = self.paddles[paddleN]
        if paddle.getSize().getP1().getY()+y< 0:
            paddle.movePaddle(-paddle.getSize().getP1().getY())
        elif paddle.getSize().getP2().getY()+y > self.w.getHeight():
            paddle.movePaddle(self.w.getHeight()-paddle.getSize().getP2().getY())
        else:
            paddle.movePaddle(y)

class Paddle:
    def __init__(self, x, size, w, color = "Black"):
        if size > w.getHeight():
            size = w.getHeight()
        self.paddle = Rectangle(Point(x-10, w.getHeight()/2-size/2), Point(x+10, w.getHeight()/2+size/2))
        self.paddle.setFill(color)
    def draw(self, w):
        self.paddle.draw(w)

    def undraw(self):
        self.paddle.undraw()
    
    def movePaddle(self, x):
        self.paddle.move(0, x)

    def getSize(self):
        return self.paddle

class Ball:
    def __init__(self, p, xv, yv, r = 15, color = "Black"):
        self.c = Circle(p , r)
        #self.c.setFill(color)
        self.xv = xv
        self.yv = yv
    def reset(self, w):
        self.moveBall(w.getWidth()/2, w.getHeight()/2)
        self.xv = random.randint(-10, 10)
        self.yv = random.randint(-10, 10)
    def moveBall(self, x, y):
        c = self.c.getCenter()
        dx = x-c.getX()
        dy = y-c.getY()
        self.c.move(dx, dy)
    def draw(self, w):
        self.c.draw(w)

    def undraw(self):
        self.c.undraw()
        
    

    
def main():
    w = GraphWin("Pongster", 600,500)
    #w.setBackground("White")
    P = Pongster(w)
    P.drawGame()
    keyUp1 = "w"
    keyDown1 = "s"
    keyUp2 = "Up"
    keyDown2 = "Down"
    w.getMouse()
    while True:
        #P.handleClick(w.getMouse())
        time.sleep(0.01)
        P.move()
        key = w.checkKey()
        if key != "":
            if key == keyUp1:
                P.movePaddle(0, -50)
            elif key == keyDown1:
                P.movePaddle(0, 50)
            if key == keyUp2:
                P.movePaddle(1, -50)
            elif key == keyDown2:
                P.movePaddle(1, 50)
            elif key == "Escape":
                break
        
    w.close()
    
if __name__ == "__main__":
    main()

#MENU?
#SETTINGS?
#SICKER GREPHIX
