from turtle import *
import random
#color("green")
up()
goto(0,0)
down()
begin_fill()
color("yellow")
circle(100)
end_fill()
colors=["Blue","Green","Red","Pink"]
for x in range (0,5):
    up();
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    goto(x,y)
    down()
    begin_fill()
    idx=random.randrange(0,len(colors)-1,1)
    color(colors[idx])
    circle(50)
    end_fill()
exitonclick()

