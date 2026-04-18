# full_name = input("Enter your full name : ")
# loop = int(input("Enter how many times to repeat :"))
# for counter in range(loop):
#     print("Hello "+ full_name)
# i=0
# while i < 10:
#     print(i)
#     i+=1
# i=10
# while not i < 0:
#     print(i)
#     i-=1

import turtle
t=turtle.Pen()
t.shape("turtle")
t.pencolor("blue")
t.speed(speed=1)
for x in range(4):
    t.forward(100)
    t.left(90)
turtle.done()
