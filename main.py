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

lista_comidas = ["Perros Calientes", "Club House", "Hamburguesas", "Parrilla", "Shawarma","Arroz Chino", "Pizza1","Pizza2"]
lista_bebinas = ["Malta","Jugo","Agua","Cerveza","Nestea","Ron","Sangria","Refresco"]
lista_postres = ["Frutas","Flan","Pudin","MilHoja","Opera","Helado","Torta","Galletas"]

variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for i in lista_comidas:
    ################# Crear CkeckBox ####################
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    i = Checkbutton(panelComida, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_comida[contador])
    i.grid(row=contador, column = 0, sticky=W)

    ################# Crear Input ####################
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panelComida, font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for i in lista_bebinas:
    ################# Crear CkeckBox ####################
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    i = Checkbutton(panelBebida, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_bebidas[contador])
    i.grid(row=contador, column = 0, sticky=W)

    ################# Crear Input ####################
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panelBebida, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable = texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)

    contador += 1

variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for i in lista_postres:
    ################# Crear CkeckBox ####################
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    i = Checkbutton(panelPostres, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_postres[contador])
    i.grid(row=contador, column = 0, sticky=W)

    ################# Crear Input ####################
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panelPostres, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable = texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1


aplicacion.mainloop() #Evita que la pantalla se cierre

