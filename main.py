from turtle import Screen
from scoreboard import Scoreboard
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

#instanciar el objeto tablero de puntos
scoreboard = Scoreboard()

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
   
   #detectar la colisión con la comida
   if snake.head.distance(food) < 15:
      food.refresh()
      scoreboard.increase_score()
      snake.extend()
   
   #Detectar la colisión con las paredes
   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
      game_is_on = False
      scoreboard.game_over()
      
   #Detectar la colisión de la cola
   for segment in snake.segments:
      if segment == snake.head:
         pass
      elif snake.head.distance(segment) < 10:
          game_is_on = False
          scoreboard.game_over()
   
   #final
screen.exitonclick() #mantiene nuestra ventana abierta

#xcor => nos da la cordenada actual de la cabeza de la serpiente