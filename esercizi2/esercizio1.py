import numpy
 
a= input("inserire il primo numero: ")
b= input ("inserire il secondo numero:")
c= input("inserire il terzo numero:")
d= input("inserire il quarto numero:")
e= input("inserire il quinto numero:")

v= numpy.array([a, b, c, d, e])
print("l'ordine inverso dei numeri inseriti è: ", v[4], v[3], v[2], v[1], v[0])