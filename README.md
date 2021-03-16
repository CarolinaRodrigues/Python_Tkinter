## Python_Tkinter

### Aula 01
**INTRODUÇÃO** 

1.Utilizando o modolo Tkinter.

2.O que é GUI??

* Graphical User Interface.

- Aplicações com forms/ windows/janelas...

- Interação mais fácial por parte do utilizador.

* Porquê o Tkinter????

- Eistem mutiplas soluções:Kivy, wxPython,etc.

- Tkinter vem integrando soluções no Python.

- Simples de aprender. Comunidade muito grande.

- Widgets mais genéricos ja incluídos.

- Aplicações multiplataforma(Windows,Mac OS, Linus )


### Aula 09

## Aula 9-> LABEL WIDGET E COMO FUNCIONA O PACK

'''
from tkinter import *

 menu_incial = Tk()
menu_inicial.title("Titulo")
label_1 = Label(menu_inicial, text = "Esse e o label 1")
label_2 = Label(menu_inicial, text = "Esse e o label 2")

cmd = Button(menu_inicial, text = "Execultar")

label_1.pack()
label_2.pack()
cmd.pack()
'''
