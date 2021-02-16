

import csv

with open('dati.txt','r') as file:
 reader = csv.reader(file)
 for row in reader:
  print(row)
print("")
print("")

with open('dati.txt', 'r') as file:
 csv_file = csv.DictReader(file)
 for row in csv_file:
  print(dict(row))

import string
import numpy as np
import matplotlib.pyplot as plt


f = open("dati.txt", 'r')


coordX = []
coordY = []



for riga in f:
    valori = str(f.readline())  
    Nval = len(valori)         
    valori = valori.strip('\n') 
    valori = valori.split(',')  
    valori = list(valori)       
    print(valori)
    coordX.append(valori[0])
    coordY.append(valori[1]) 

f.close()  

print ("X: ",coordX)
print ("Y: ",coordY)


coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)


print(type(coordX))
print(type(coordY))

plt.scatter(coordX,coordY)

from guizero import *

def do_nothing():

   open("dati.txt", 'r')

app = App(title="Keypad example", width=100, height=90, layout="grid")

button1 = PushButton(app, command=do_nothing, text="1", grid=[0,0])
app.display()

plt.show()