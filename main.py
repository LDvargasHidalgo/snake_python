from turtle import Screen
from snake import Snake
from food import Food

import time

#crear el escenario
screen = Screen()
screen.setup(width=600, height=600) #tamaño de la pantalla
screen.bgcolor("black") #color de la ventana
screen.title("Prográmate Snake")

screen.tracer(0)

#instanciar el objeto serpiente
snake = Snake()

#instanciar el objeto comida
food = Food()

#movimientos serpiente
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#mientras el juego este funcionando
game_is_on = True

while game_is_on:
   screen.update()
   time.sleep(0.2)
   
   snake.move()
   
   #final
screen.exitonclick() #mantiene nuestra ventana abierta