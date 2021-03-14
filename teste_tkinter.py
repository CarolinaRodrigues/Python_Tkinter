from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Calculadora") 
menu_inicial.geometry("500x500+200+500") #tamanho da janela 
menu_inicial.resizable(True, True)
#menu_inicial.minsize(width = 500, height = 300)
#menu_inicial.maxsize(width = 800, height = 500)
#menu_inicial.state()
menu_inicial.iconbitmap("images/icon.ico")
menu_inicial['bg'] = "silver"

def soma():
	print("somar dois numeros")
def subtrair():
	print("subtrair dois numeros")
def multiplicar():
	print("multiplicar dois numeros")
def dividir():
	print("dividir dois numeros")

#Label
label1 = Label(
	menu_inicial,
	text = "Calculadora",
	font = "Times 20", 
	bg = "silver",
	fg ='White'
	#bd= 5,
	#relief = 'solid'
	).pack()
#Botões das operações '+' / '-' / '*' / '/'
btn1 = Button(menu_inicial, text = "+", command = soma )


#btn.grid(row = 0, column = 0)

btn2 = Button(menu_inicial, text = "-", command = subtrair)
#btn1.grid(row = 1, column = 0)

btn3 = Button(menu_inicial, text = "*", command = multiplicar)
#btn2.grid(row = 2, column = 0)

btn4 = Button(menu_inicial, text = "/", command = dividir)
#btn3.grid(row = 3, column = 0)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

menu_inicial.mainloop()




#Creating a Label Widget
#myLabel1 = Label(menu_inicial, text = "Calculadora--------------------- ")
#myLabel2 = Label(menu_inicial, text = "From :  Carol & Philipe")
#myLabel3 = Label(menu_inicial, text = "Projetinho")

#myLabel1.grid(row = 0, column = 0)
#myLabel2.grid(row = 1, column = 0)
#myLabel3.grid(row = 2, column = 0)