import colorgram
import random
import turtle as turtle_module

color_list = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228),
              (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138),
              (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156),
              (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203),
              (206, 184, 190), (37, 73, 84), (45, 74, 63), (48, 66, 80), (115, 134, 136), (183, 193, 202)]


tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list) )
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(98)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()