from turtle import Turtle
import random  #generar posición aleatoria de la comida



class Food(Turtle):  #indico de quien va a heredar 

    def __init__(self):
        super().__init__()  #que herede de turtle y coja todo lo posible,  con init cojo todo de turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.refresh()  #cambiar la posición de la comida de forma aleatoria

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)