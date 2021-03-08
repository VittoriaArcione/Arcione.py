import numpy

a= (input("inserisci un numero per sapere quante volte è presente nella lista: "))
v= numpy.array([4, 4, 7, 5, 2])

m = "0"


for numero in v:
    if v.count(numero) > v.count(m):
         m= numero
