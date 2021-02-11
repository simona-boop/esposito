import guizero
from guizero import App, Text, TextBox, PushButton
import string 
import numpy as np
import matplotlib.pyplot as plt


f = open("dati.txt", 'r')

coordX = []
coordY = []

def bottone0():
    for riga in f:
        valori = str(riga)
        Nval = len(valori)
        valori = valori.strip('\n')
        valori = valori.split(',')
        valori = list(valori)
        print(valori)
        coordX.append(int(valori[0]))
        coordY.append(int(valori[1]))


    print ("X: ",coordX)
    print ("Y: ",coordY)


    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)


    print(type(coordX))
    print(type(coordY))



plt.plot(coordX,coordY)
plt.ylabel('some numbers')
plt.show() 

app = App(title='interfaccia')

hello_text = Text(app, text='interfaccia', font='Arial', size=40)

whatever = TextBox(app, width=30, multiline=True, height=2)
whatever.value='interfaccia/grafico'

push = PushButton(app, text='grafico', command = bottone0)
push.width=8
push.height=3


app.display()
