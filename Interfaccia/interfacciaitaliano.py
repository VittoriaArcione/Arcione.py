import turtle
from tkinter import*
from tkinter import messagebox
def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku?')
root=Tk()
root.geometry('600x600')
root.title("GENERATORE DI HAIKU AUTOMATICO")
lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", font=(20))
lbl.pack()
b=Button(root, text="Cliccami per le istruzioni d'uso", command=istruzioni)
b.pack()

