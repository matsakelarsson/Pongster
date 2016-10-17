from graphics import *

class Button:
    def __init__(self, w, P1, P2, text):
        self.w = w
        self.button = Rectangle(P1, P2)
        self.buttonText = Text(self.button.getCenter(), text)
        self.button.setFill("Cyan")
        self.buttonText.setTextColor("Red")
        self.drawn = False

    def draw(self):
        self.button.draw(self.w)
        self.buttonText.draw(self.w)
        self.drawn = True
    def undraw(self):
        if self.drawn:
            self.button.undraw()
            self.buttonText.undraw()
            self.drawn = False
    def handleClick(self, p):
        if self.drawn:
            if p.getX() > self.button.getP1().getX() and p.getX() < self.button.getP2().getX() and p.getY() > self.button.getP1().getY() and p.getY() < self.button.getP2().getY():
                return self.buttonText.getText()
            


def main():
    w = GraphWin("Menu", 600, 500)
    buttons = []
    buttons.append(Button(w, Point(100, 100), Point(300, 200), "a!"))
    buttons.append(Button(w, Point(100, 300), Point(300, 400), "b!"))

    for button in buttons:
        button.draw()
    for _ in range(10):
        p = w.getMouse()
        for button in buttons:
            print button.handleClick(p)
    w.close()
    
if __name__ == "__main__":
    main()
        
    
