import turtle

def drShape(avatar):
    for i in range(25):
        for i in range(4):
            avatar.forward(300)
            avatar.right(135)
        avatar.right(10)
def colorChoice():
        window = turtle.Screen()
        window.bgcolor("black")
        
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("red")
        brad.speed(9)
        return brad
        
def drBrad():   
        drShape(colorChoice())
            
        # window.exitonclick()
    
drBrad()
