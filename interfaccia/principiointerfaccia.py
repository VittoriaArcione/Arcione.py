from guizero import *
def get_file():
    if etichettaA=="dati.txt":
     open("dati.txt", "r")

app = App(title="CONFIGURAZIONE GRAFICA")
output = TextBox(app, width=80, height=10, multiline=True)
etichettaA = Text(app, text="scrivi dati.txt")
paramA = TextBox(app)

pushB = PushButton(app, text="apri file",command = get_file)
app.display()