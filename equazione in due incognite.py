
print("troviamo il valore di x nell'equazione di primo grado a due incognite ax+b=0")

a = float(input("inserire variabile uno: "))
b = float(input("inserire variabile due: "))
c = float(-b/a)
e = float(b/-a)
d = max(a,b,c)
u = float(-a/b)


print("il valore di x è")

if a > 0 :
 print (c)

elif a < 0 :
  print (e)


print ("il più grande tra i valori è ") 
print (d)

print("se invertiamo le variabili il valore di x diventa")

print (u)
