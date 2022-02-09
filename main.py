from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game by Rajesh Sharma")

paddle = Turtle()
paddle.shape("square")
paddle
paddle.shapesize(stretch_wid=5, stretch_len=1)

screen.exitonclick()
