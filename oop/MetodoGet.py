class libri:

    
    titolo = 1
    copertina = True
    numerolibri = 0

  
    def __init__(self,proprietario, autore, numeroPagine, colore):

     
        self.proprietario = proprietario
        self.autore = autore
        self.numeroPagine = numeroPagine
        self.colore = colore
        
        libri.numerolibri +=1

    
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n autore: {self.autore}\n numeroPagine: {self.numeroPagine}\n colore: {self.colore}\n copertina: {self.copertina}' 
    
gennaro = libri("gennaro","Arthur Conan Doyle","1600","giallo")

giulia = libri("giulia","Agatha Christie","567", "grigio")

print("Il tipo di variabile costruita è:")
print(gennaro)
print(giulia)

print("\nLa singola scheda è:")
print (gennaro.scheda())
print (giulia.scheda())
print("\nlibri totali: ",libri.numerolibri)

print("\nVisualizzazione dizionario")
print(gennaro.__dict__)
print(giulia.__dict__)

