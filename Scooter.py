giorno = int(input("Inserire il numero di giorni in cui si desidera affittare un motorino: "))
risultato = giorno - 4
abx = 40
aby = 160
risultatodue = risultato * abx
risultatotre = risultatodue + aby 

if giorno == 1 :
  print("Il costo del noleggio per un giorno è di 45,00€")
  
elif giorno == 2 :
  print("Il costo del noleggio per due giorni è di 80,00€")
  
elif giorno == 3 :
  print("Il costo del noleggio per tre giorni è di 120,00€")
  
elif giorno == 4 :
  print("Il costo del noleggio per quattro giorni è di 160,00€")
  
elif giorno > 4 :
    print(str("Il costo del noleggio ammonta a ") + str(risultatotre) + str(",00") +str("€"))
