import turtle, random

def set_position(line, curr_pos):
    if line == 1:
        timmy.setpos(-230, -240)
    else:
        timmy.setpos(curr_pos[0] - 500, curr_pos[1] + 50)

def draw_line(line):
    timmy.penup()
    set_position(line, timmy.position())
    for i in range(10):
        timmy.pendown()
        timmy.dot(30, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

# import colorgram as cg

# colors = cg.extract("image.jpg", 20)
# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_list.append(rgb)

color_list = [(187, 254, 214), (242, 195, 228), (228, 216, 205), (253, 201, 70), (204, 236, 253), (127, 141, 239), (103, 230, 253), (220, 68, 15), (241, 160, 72), (94, 10, 4), (79, 11, 47), (250, 69, 36), (78, 35, 105), (26, 4, 108), (191, 93, 229), (22, 127, 248), (224, 157, 27), (228, 118, 198), (45, 25, 124), (43, 108, 186)]

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
line = 1
for i in range(10):
    draw_line(line)
    line += 1

screen = turtle.Screen()
# print(screen.screensize())
screen.exitonclick()
# print(color_list)