# Aula 31 -> ADICIONAR IMAGEM A UM LAYOUT
from tkinter import * 


root = Tk()

img = PhotoImage(file = "images/iconTotoro_nova.png")




#widgets

#layout

label_imagem = Label(root, image=img).pack()

root.mainloop()