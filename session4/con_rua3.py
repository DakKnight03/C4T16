from turtle import *
shape("turtle")
speed(-1)
color("yellow")
fillcolor("red")
begin_fill()
for i in range(6):
    # for i in range(360):
    #     forward(1)
    #     left(1)
    circle(80)
    right(60)
end_fill()
mainloop()