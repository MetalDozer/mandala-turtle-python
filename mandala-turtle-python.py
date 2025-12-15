#!/bin/env python3
import turtle

pantalla = turtle.Screen()
pantalla.setup(800, 800,0,0)
pantalla.mode("standard")
pantalla.bgcolor("black")

tortuga = turtle.Turtle()
tortuga.color("red")
tortuga.pensize(2)
tortuga.speed(0)

def hacer_cuadrado(largo=50):
    for _ in range(4):
        tortuga.forward(largo)
        tortuga.left(90)

def hacer_vueltas(cantidad=16, largo=50):
    for _ in range(cantidad):
        hacer_cuadrado(largo)
        tortuga.left(360/cantidad)

def hacer_mandala(longitud, exponente, circulos=3):
    for _ in range(circulos):
        hacer_vueltas(largo=longitud)
        longitud *= exponente

if __name__ == "__main__":
    hacer_mandala(50,1.7,5)
    pantalla.exitonclick()
