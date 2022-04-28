from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):   #constructor del tablero
        super().__init__()
        self.score = 0  #atributo
        self.goto(0, 270)
        self.color("white")
        self.update_score()  #llamar la variable definida para que aparezca el tablero de puntos
        self.hideturtle()

    def update_score(self):   #metodo para pintar el tablero de puntos
        self.write(f"el puntaje es: {self.score}",font=("Arial", 20, "bold"), align="center")   #la f se usa para concatenar textos.


    def increase_score(self):
        self.clear()
        self.score += 1  #para que sume los puntos
        self.update_score() 


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" ,font=("Arial", 20, "bold"), align="center")   #la f se usa para concatenar textos.

