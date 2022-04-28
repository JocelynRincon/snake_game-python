from turtle import Turtle
#screem para crear el escenario   
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0  

class Snake:

    def __init__(self):  #def es para crear una función, el init es el contructor
            self.segments = []    #atributo
            self.create_snake()  #método para crear la serpiente
            self.head = self.segments[0]
    
    #creación del cuerpo de la serpiente


    
    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()  #para que no cree la línea
            snake_segment.goto(position)
            self.segments.append(snake_segment)  #append permite agrgar cosas en una lista

    def move(self):
        #movimiento
        for seg_num in range(len(self.segments) -1, 0, -1):  #range:hace el rango de los elementos
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)  #que vaya hacia adelante
        #self.segments[0].left(90)   #que gire a la izquierda 90°

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

#SE HICIERON CONSTANTES PARA DARLE UN USO GLOBAL Y EL ANALISIS VA A SER MAS LAEGIBLE DEL CODIGO. LEFT,RIGHT,DOWN,UP(MAYUSCULAS)





#poo= programacion orientada a objetos: es un pardigma, un conjunto de reglas.
#la clase es la plantilla con la que armo el objeto y el objeto es lo que nace de la clase y puede usarse como desee, cambiando cosas.
#constructor: permite que se ejecute o crear un objeto

#90 up
#180 left
#270 down