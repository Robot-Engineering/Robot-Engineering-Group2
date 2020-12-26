import turtle as t
class  DrawLine():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sim(self):
        t.setpos(self.x,self.y)
