import turtle as t


class DrawCircle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r


    def set(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def draw(self):
        t.pensize(3)
        t.pencolor('black')
        t.pu()
        t.goto(self.x,self.y)
        t.pd()
        t.circle(self.r)
        t.show
        
