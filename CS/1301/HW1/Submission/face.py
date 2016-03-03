#Sagar Laud
#slaud3@mail.gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.

from myro import *
win = GraphWin("Sagar's Window", 200,200)

p1 = Point (100,100)
p2 = Point (400,400)
p3 = Point (50, 100)
p4 = Point(-1, 75)
p5 = Point(35, 35)
p6 = Point(-50, 100)
p7 = Point(0, 0)
p8 = Point(50, 50)
p9 = Point(100,130)
p10= Point(30, 130)

c = Circle (p1, 100)
c.draw(win)
color = color_rgb(255, 175, 175)
c.setFill(color)


o = Oval(p3, p4)
o.draw(win)
color = color_rgb(255,255,255)
o.setFill(color)
o.move(35, -30)

o = Oval(p3, p4)
o.draw(win)
color = color_rgb(255,255,255)
o.setFill(color)
o.move(115, -30)

l = Line(p1, p5)
l.draw(win)
l.move(-5, 90)

l= Line(p6, p5)
l.draw(win)
l.move(145, 90)

l = Line(p8, p7)
l.draw(win)
l.move(95, 75)

l= Line(p9, p10)
l.draw(win)
l.move(45,-5)

c = Circle(p1, 5)
c.draw(win)
color = color_rgb(0,255,0)
c.setFill(color)
c.move(-25, -43)


c = Circle(p1, 5)
c.draw(win)
color = color_rgb(0,255,0)
c.setFill(color)
c.move(25, -43)

o= Oval(p4, p5)
o.draw(win)
color = color_rgb(100,100,0)
o.setFill(color)
o.move(20, 40)

r = Rectangle(p5, p8)
r.draw(win)
color = color_rgb(0,0,255)
r.setFill(color)
r.move(-5, 50)






