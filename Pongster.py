from graphics import *
import random

class Pongster:
    def __init__(self, w):
        self.balls = []
        self.balls.append(Ball(w))
        self.paddles = []
        
        self.paddles.append(Paddle(w.getWidth()/8, 200, w))
        self.paddles.append(Paddle(w.getWidth()/8*7, 300, w))

    def move(self):
        for ball in self.balls:
            
            x = ball.c.getCenter().getX()
            y = ball.c.getCenter().getY()
            width = ball.w.getWidth()
            height = ball.w.getHeight()
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
                if ((x >= p.getP2().getX()+r and x + ball.xv <= p.getP2().getX()+r) or (x <= p.getP1().getX()-r and x + ball.xv >= p.getP1().getX()-r)) and (y + ball.yv >= p.getP1().getY() and y + ball.yv <= p.getP2().getY()):
                    ball.xv = -ball.xv
                #TODO: maek stronk in Y DIRECTION pls...
            ball.c.move(ball.xv, ball.yv)
    def addBall(self, B):
        self.balls.append(B)

    def movePaddle(self, paddleN, x):
        self.paddles[paddleN].movePaddle(x)

class Paddle:
    def __init__(self, x, size, w):
        if size > w.getHeight():
            size = w.getHeight()
        self.paddle = Rectangle(Point(x-10, w.getHeight()/2-size/2), Point(x+10, w.getHeight()/2+size/2))
        self.paddle.draw(w)

    def movePaddle(self, x):
        self.paddle.move(0, x)

    def getSize(self):
        return self.paddle

class Ball:
    def __init__(self, w, p = Point(50, 20), xv = -2, yv = 0, r = 10):
        self.c = Circle(p , r)
        self.c.draw(w)
        self.xv = xv
        self.yv = yv
        self.w = w
    

    
def main():
    w = GraphWin("Pongster", 600,500)
    P = Pongster(w)
    P.addBall(Ball(w))
    keyUp = w.getKey()
    keyDown = w.getKey()
    for i in range(10000):
        time.sleep(0.01)
        P.move()
        key = w.checkKey()
        if key != "":
            if key == keyDown:
                P.movePaddle(0, 50)
            elif key == keyUp:
                P.movePaddle(0, -50)
    w.close()
if __name__ == "__main__":
    main()

#TODO: maek ather paddle moof pls
#MENU?
#SETTINGS?
#SICKER GREPHIX
