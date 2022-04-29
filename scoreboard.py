from turtle import Turtle

ALIGN = "center"
FONT ="Arial", 24, "italic"

class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0  #Atributo caracteristicas de los metodos y los metodos son las acciones
        self.goto(-220,268)
        self.color("white")
        self.update_score()
        self.hideturtle()

#Metodo actualizar el tablero
    def update_score(self):
        self.write(f"Score: {self.score}",font=FONT, align=ALIGN)
        
    def increase_score(self):
        self.color("white")
        self.clear()
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)       
        self.write("¡GAME OVER ! ",font=FONT, align=ALIGN)
       
        
        
        
        
    