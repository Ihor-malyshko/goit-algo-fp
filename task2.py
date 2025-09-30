import turtle

def draw_branch(t, length, angle, depth):
    if depth == 0:
        return
    
    t.forward(length)
    
    position = t.position()
    heading = t.heading()
    
    t.left(angle)
    draw_branch(t, length * 0.75, angle, depth - 1)
    
    t.setposition(position)
    t.setheading(heading)
    
    t.right(angle)
    draw_branch(t, length * 0.75, angle, depth - 1)
    
    t.setposition(position)
    t.setheading(heading)

def create_pythagoras_tree(depth):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Оголене дерево Піфагора. рівень рекурсії = {depth}")
    screen.setup(800, 600)
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    
    draw_branch(t, 100, 30, depth)
    
    t.hideturtle()
    screen.exitonclick()



depth = int(input("рівень рекурсії?"))
create_pythagoras_tree(depth)


