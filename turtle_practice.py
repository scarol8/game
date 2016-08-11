#import turtle             # Allows us to use turtles


from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#wn = turtle.Screen()      # Creates a playground for turtles
#alex = turtle.Turtle()    # Create a turtle, assign to alex

#alex.forward(50)          # Tell alex to move forward by 50 units
#alex.left(90)             # Tell alex to turn by 90 degrees
#alex.forward(30)          # Complete the second side of a rectangle

#mainloop()             # Wait for user to close window
