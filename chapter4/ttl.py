import turtle as trtl


def drawSpiral(turtle, line_length):
    if line_length > 0:
        turtle.forward(line_length)
        turtle.right(70)
        drawSpiral(turtle, line_length-5)


def second():
    turtle = trtl.Turtle()
    screen = trtl.Screen()
    drawSpiral(turtle, 200)
    screen.exitonclick()


def drawTree(branch_length, turtle, pen_size):
    if branch_length > 5:
        turtle.pensize(pen_size)
        turtle.forward(branch_length) # go forward the entire branch length
        turtle.right(20) # turn right by 20 degrees
        drawTree(branch_length - 15, turtle, pen_size / 1.5) # start another branch
        turtle.left(40) # turn left by 40 degrees (aka, 20 degrees left of starting direction)
        drawTree(branch_length - 15, turtle, pen_size / 1.5) # start another branch
        turtle.right(20) # return the turtle's direction to straight
        turtle.backward(branch_length) # retrace backwards to either continue drawing more branches or terminate


def main():
    turtle = trtl.Turtle()
    screen = trtl.Screen()
    turtle.left(90) # turn 90 degrees left (vertically up)
    turtle.up() # IDK what this does
    turtle.backward(100) # move the turtle backwards 100 pixels
    turtle.down() # the opposite of up?
    turtle.color("green") # green color to the tree
    starting_pen_size = 10
    drawTree(75, turtle, starting_pen_size) # begin drawing branches, I assume.
    screen.exitonclick()


if __name__ == "__main__":
    main()
