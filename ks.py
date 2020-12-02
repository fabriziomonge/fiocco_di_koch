from turtle import *

def curva_koch(dimensione, ordine):
    if ordine > 0:
        for t in [60, -120, 60, 0]:
            curva_koch(dimensione/3, ordine-1)
            left(t)
    else:
        forward(dimensione)



color("sky blue", "white")
bgcolor("blue")

ordine = 7
colore_linea = "sky blue"
colore_riempimento = ["white", "sky blue", "white"]


lista_dimensioni = [700,400,200]




for i in range (3):
    color(colore_linea, colore_riempimento[i])
    dimensione=lista_dimensioni[i]
    penup()
    backward(dimensione/1.732)
    left(30)
    pendown()


    tracer(100)
    hideturtle()

    begin_fill()

    for i in range(3):
        curva_koch(dimensione, ordine)
        right(120)

    end_fill()
    right(30)
    penup()
    forward(dimensione/1.732)
    pendown()

 
    update()


