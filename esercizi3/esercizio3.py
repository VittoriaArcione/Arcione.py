from numpy import median
dizionario =  {"mario": [6, 6, 7, 4], "giovanni": [4, 6, 5, 7], "paola": [9, 6, 8, 8]}

print("la media dei voti di mario è: ", median(dizionario["mario"]))
print("la media dei voti di giovanni è: ", median(dizionario["giovanni"]))
print("la media dei voti di paola è: ", median(dizionario["paola"]))