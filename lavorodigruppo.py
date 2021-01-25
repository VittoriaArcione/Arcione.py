import csv

with open('ello.txt','r') as file:
 reader = csv.reader(file)
 for row in reader:
  print(row)
print("")
print("")

with open('ello.txt', 'r') as file:
 csv_file = csv.DictReader(file)
 for row in csv_file:
  print(dict(row))

import string
import numpy as np
import matplotlib.pyplot as plt


f = open("ello.txt", 'r')


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



plt.plot(coordX,coordY)

plt.show()