import turtle
bob = turtle.Turtle()

def main():
    square()
    bob.right(90)
    bob.penup()
    bob.forward(150)
    bob.pendown()
    square()


def square():
    bob.color("blue", "cyan") # The second color is the fill color
    bob.begin_fill()
    for i in range(4):
        bob.forward(100)
        bob.left(90)
    bob.end_fill()

main()
turtle.done()