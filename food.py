
from turtle import Turtle
import random


class Food(Turtle):
        
     def __init__(self):  #definir el constructor
         super().__init__()#herencia,  food hereda de turtle
         self.shape("circle")
         self.penup()
         self.shapesize(stretch_len=0.5, stretch_wid=0.5)
         self.color("red")
         self.refresh()
         
         
       #cambia la posición de la comida de manera aleatoria  
     def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
        
         
         
    