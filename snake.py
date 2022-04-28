#importo librerias 
from tkinter import LEFT, RIGHT
from turtle import Turtle, forward

#para evitar la repeticion del codigo se realiza un ciclo for
# se defini la variable position puse un array y unas tuplas con la info de las cordenadas que quiero que tenga

#creacion del cuerpo de la serpiente
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT  = 0

class Snake:

    #creacion del constructor
    def __init__(self):
        self.segments = [] #atributo
        self.create_snake() #metodo
        self.head  = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        snake_segment = Turtle("circle")
        snake_segment.color("yellow")
        snake_segment.penup() #quitar  la linea del centro 
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
          
            

    #este for solo funciona para ir hacia adelante   
    #aqui se define el moviemiento de la serpiente 
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)


#MOVIMIENTOS DE LA SERPIENTE
    def up(self):
        if self. head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
           if self.head.heading() !=UP:
            self.head.setheading(DOWN)
        
    def left(self):
           if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
           if self.head.heading() !=LEFT:
                self.head.setheading(RIGHT)
        
        
    

