from turtle import *
number = int(input("enter a number: "))
shape("turtle")
speed(-1)
for i in range(number):
    forward(100)
    left(360 / number)
mainloop()