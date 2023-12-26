from tkinter import *

aplicacion = Tk() #Se inicializa TKinter

aplicacion.geometry("1020x630+0+0")  #Se cofigura tamano de la ventana

aplicacion.resizable(0,0) #Ni en el eje x ni en el eje y se podra expandir la ventana

aplicacion.title("Restaurant xxx - Sistema de Facturacion")

aplicacion.config(bg='azure') #Se configura color de fondo de la ventana

############################ Parte Superior#########################################
panelSuperior = Frame(aplicacion, bd=1, relief=FLAT)
panelSuperior.pack(side=TOP) #Ubicacion del Frame
etiqueta_titulo = Label(panelSuperior, text="Sistema de Facturacion", fg="black", font=("Dosis",48), background="azure",width=27)
etiqueta_titulo.grid(row=0,column=0) #Desde donde comenzara el Frame

########################### Panel Izquierdo ######################################

panelIzquiero = Frame(aplicacion, bd=1, relief=FLAT)
panelIzquiero.pack(side=LEFT)

panelCosto = Frame(panelIzquiero, bd=1, relief=FLAT)
panelCosto.pack(side=BOTTOM)

panelComida = LabelFrame(panelIzquiero,text= "Comida",font=("Dosis",19,"bold"), bd=1, relief=FLAT)
panelComida.pack(side=LEFT)

panelBebida = LabelFrame(panelIzquiero,text= "Bebidas",font=("Dosis",19,"bold"), bd=1, relief=FLAT)
panelBebida.pack(side=LEFT)

panelPostres = LabelFrame(panelIzquiero,text= "Postres",font=("Dosis",19,"bold"), bd=1, relief=FLAT)
panelPostres.pack(side=LEFT)

########################### Panel Derecha #######################################

panelDerecha = Frame(aplicacion, bd=1, relief=FLAT)
panelDerecha.pack(side=RIGHT)

panelCalculadora = LabelFrame(panelDerecha,text= "Postres", bd=1, relief=FLAT, bg="azure")
panelCalculadora.pack(side=TOP)

panelRecibo = LabelFrame(panelDerecha,text= "Postres", bd=1, relief=FLAT, bg="azure")
panelRecibo.pack(side=TOP)

panelBotones = LabelFrame(panelDerecha,text= "Postres", bd=1, relief=FLAT, bg="azure")
panelBotones.pack(side=TOP)








aplicacion.mainloop() #Evita que la pantalla se cierre

