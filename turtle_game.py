#This creates the window for the game
import turtle
wn = turtle.Screen()
wn.title("Super Shape Turtle")
wn.bgcolor("black")

#Create turtle
shape_turtle=turtle.Turtle()
shape_turtle.color("white")
shape_turtle.shape("turtle")
shape_turtle.speed(7)

#Move to starting position
shape_turtle.penup()
shape_turtle.goto(-100,120)
shape_turtle.pendown()

#Get input for the shape the user wants to draw
vertices = int(input("How many vertices do you want the shape to have? Please enter a number between 3-10:"))

while vertices <= 2 or vertices >= 11:
    print("Please enter an appropriate value")
    vertices = int(input("How many vertices do you want the shape to have?"))

#Output shape the user has requested
if vertices == 3:
    print("Drawing Triangle")
elif vertices == 4:
    print("Drawing Square")
elif vertices == 5:
    print("Drawing Pentagon")
elif vertices == 6:
    print("Drawings Hexagon")
elif vertices == 7:
    print("Drawing Heptagon")
elif vertices == 8:
    print("Drawing Octagon")
elif vertices == 9:
    print("Drawing Nonagon")
elif vertices == 10:
    print("Drawing Decagon")

#Establish variables to help with rendering of shape
angle_sum = (vertices-2)*180
angle = angle_sum/vertices
turn = 180 - angle
vertices_left = vertices

#Draw the shape in the window
while vertices_left > 0:
    shape_turtle.forward(100)
    shape_turtle.right(turn)
    vertices_left = vertices_left-1
print("Complete")

wn.mainloop()