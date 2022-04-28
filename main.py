#todo lo que no tiene que ver con la serpiente es decir le motor de juego y el escenario.
from turtle import Screen  #Screen aquí es una clase en la línea 7 se crea el objeto.
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard



#crear escenario; instanciar es tomar todas las variables de un objeto
screen = Screen()  #instanciar el objeto
screen.setup(width=600, height=600) #setup es un metdo que esta dentro de Screen
screen.bgcolor("black")
screen.title("Prográmate snake")

screen.tracer(0)  #quitar animación de movimiento


#instanciar el objeto serpiente
snake = Snake()

#instanciar el objeto comida
food = Food()

#instanciar el objeto tablero de puntos
scoreboard = Scoreboard()

#movimiento serpiente
screen.listen()
screen.onkey(snake.up, "Up")

screen.listen
screen.onkey(snake.down, "Down")

screen.listen
screen.onkey(snake.left, "Left")

screen.listen
screen.onkey(snake.right, "Right")




game_is_on = True  #en python siempre debe ir en mayuscula True

while game_is_on:
    screen.update() #despues del tracer los cuadros no se movian, update actualiza para que se mueva como debe
    time.sleep(0.1)   #aumentar o disminuir la velocidad
    
    snake.move()

#detecar colisión con comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

#detectar las paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:       #la pared mide 300 se le pone 280 para que se vea el efecto que murió
        game_is_on = False
        scoreboard.game_over()


        #detectar la colisión de la cola
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    





screen.exitonclick()  #para que al abrir la ventana se cierre cuando le dé click
