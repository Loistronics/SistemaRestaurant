from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox

operador = '' #Donde se almacena todo lo presionado en la calculadora

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero_signo):
    global operador
    operador = operador + numero_signo
    pantallaCalculadora.delete(0,END)
    pantallaCalculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    pantallaCalculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    pantallaCalculadora.delete(0,END)
    pantallaCalculadora.insert(END, resultado)
    operador = ''

def revisarCheck():
    x = 0
    for i in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1
    x = 0
    for i in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1
    x = 0
    for i in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    subTotalComida = 0
    p = 0
    for i in texto_comida:
        subTotalComida = subTotalComida + (float(i.get()) * precios_comida[p])
        p += 1
    print(subTotalComida)

    subTotalBebida = 0
    p = 0
    for i in texto_bebidas:
        subTotalBebida = subTotalBebida+ (float(i.get()) * precios_bebida[p])
        p += 1
    print(subTotalBebida)

    subTotalPostre = 0
    p = 0
    for i in texto_postres:
        subTotalPostre = subTotalPostre + (float(i.get()) * precios_postres[p])
        p += 1

    subTotal = subTotalComida + subTotalBebida + subTotalPostre
    impuestos = subTotal * 0.15
    total = subTotal + impuestos

    variableCostoComida.set(f"${round(subTotalComida)}")
    variableCostoBebida.set(f"${round(subTotalBebida)}")
    variableCostoPostre.set(f"${round(subTotalPostre)}")

    variableSubTotal.set(f"${round(subTotal)}")
    variableImpuesto.set(f"${round(impuestos)}")
    variableTotal.set(f"${round(total)}")

def factura():
    textoRecibo.delete(1.0, END)
    numeroFactura = f"N# {random.randint(10000, 100000)}"
    fecha = datetime.datetime.now()
    fechaFactura = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    textoRecibo.insert(END, f"Datos: \t{numeroFactura}\t\t{fechaFactura}\n")
    textoRecibo.insert(END, f"*" * 63 + "\n")
    textoRecibo.insert(END, "Articulo\t\tCantidad\t\tCosto\n")
    textoRecibo.insert(END, "-" * 75 + "\n")

    x = 0
    for i in texto_comida:
        if i.get() != '0':
            textoRecibo.insert(END, f"{lista_comidas[x]}\t\t{i.get()}\t\t${int(i.get()) * precios_comida[x]}\n")
        x+=1
    x = 0
    for i in texto_bebidas:
        if i.get() != '0':
            textoRecibo.insert(END, f"{lista_bebinas[x]}\t\t{i.get()}\t\t${int(i.get()) * precios_bebida[x]}\n")
        x += 1
    x = 0
    for i in texto_postres:
        if i.get() != '0':
            textoRecibo.insert(END, f"{lista_postres[x]}\t\t{i.get()}\t\t${int(i.get()) * precios_postres[x]}\n")
        x += 1

    textoRecibo.insert(END, "-" * 75 + "\n")
    textoRecibo.insert(END,f"Costo Comida:\t\t\t{variableCostoComida.get()}\n")
    textoRecibo.insert(END, f"Costo Bebida:\t\t\t{variableCostoBebida.get()}\n")
    textoRecibo.insert(END, f"Costo Postre:\t\t\t{variableCostoPostre.get()}\n")
    textoRecibo.insert(END, "-" * 75 + "\n")
    textoRecibo.insert(END, f"SubTotal:\t\t\t{variableSubTotal.get()}\n")
    textoRecibo.insert(END, f"Impuesto:\t\t\t{variableImpuesto.get()}\n")
    textoRecibo.insert(END, f"Total:\t\t\t{variableTotal.get()}\n")
    textoRecibo.insert(END, "-" * 75 + "\n")

def guardarFactura():
    infoRecibo = textoRecibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(infoRecibo)
    archivo.close()
    messagebox.showinfo("Informacion","La factura fue guardada con Exito")

def resetearPantalla():
    textoRecibo.delete(0.1,END)
    ### Texto de los Inputs a 0 ########
    for i in texto_comida:
        i.set('0')
    for i in texto_bebidas:
        i.set('0')
    for i in texto_postres:
        i.set('0')
    ### Input solo de lectura ############
    for i in cuadros_comida:
        i.config(state=DISABLED)
    for i in cuadros_bebidas:
        i.config(state=DISABLED)
    for i in cuadros_postres:
        i.config(state=DISABLED)
    ### Contenido de los checkBox ##########
    for i in variables_comida:
        i.set(0)
    for i in variables_bebidas:
        i.set(0)
    for i in variables_postres:
        i.set(0)

    variableCostoComida.set('')
    variableCostoBebida.set('')
    variableCostoPostre.set('')
    variableSubTotal.set('')
    variableTotal.set('')
    variableImpuesto.set('')


aplicacion = Tk() #Se inicializa TKinter

aplicacion.geometry("1200x630+0+0")  #Se cofigura tamano de la ventana

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

panelCosto = Frame(panelIzquiero, bd=1, relief=FLAT, bg='azure4', padx = 100)
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

panelCalculadora = LabelFrame(panelDerecha,text= "Calculadora", bd=1, relief=FLAT, bg="azure")
panelCalculadora.pack(side=TOP)

panelRecibo = LabelFrame(panelDerecha,text= "Recibo", bd=1, relief=FLAT, bg="azure")
panelRecibo.pack(side=TOP)

panelBotones = LabelFrame(panelDerecha, bd=1, relief=FLAT, bg="azure")
panelBotones.pack(side=TOP)

lista_comidas = ["Perros Calientes", "Club House", "Hamburguesas", "Parrilla", "Shawarma","Arroz Chino", "Pizza1","Pizza2"]
lista_bebinas = ["Malta","Jugo","Agua","Cerveza","Nestea","Ron","Sangria","Refresco"]
lista_postres = ["Frutas","Flan","Pudin","MilHoja","Opera","Helado","Torta","Galletas"]

variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for i in lista_comidas:
    ################# Crear CkeckButton ####################
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    i = Checkbutton(panelComida, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_comida[contador], command=revisarCheck)
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
    ################# Crear CkeckButton ####################
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    i = Checkbutton(panelBebida, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_bebidas[contador], command=revisarCheck)
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
    ################# Crear CkeckButton ####################
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    i = Checkbutton(panelPostres, text=i.title(), font=("Dosis",19,"bold"),onvalue=1, offvalue=0, variable = variables_postres[contador], command=revisarCheck)
    i.grid(row=contador, column = 0, sticky=W)

    ################# Crear Input ####################
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panelPostres, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable = texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

##############################################################################################

#Variables
variableCostoComida = StringVar()
variableCostoBebida = StringVar()
variableCostoPostre = StringVar()

variableSubTotal = StringVar()
variableImpuesto = StringVar()
variableTotal = StringVar()

#Etiquetas de Costo y campos de Entrada
etiquetaCostoComida = Label(panelCosto, text = 'Costo Comida' , font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaCostoComida.grid(row=0, column=0)
textoCostoComida = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableCostoComida)
textoCostoComida.grid(row=0 ,column = 1, padx = 41)

etiquetaCostoBebida = Label(panelCosto, text = 'Costo Bebida',  font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaCostoBebida.grid(row=1, column=0)
textoCostoBebida = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableCostoBebida)
textoCostoBebida.grid(row=1 ,column = 1, padx = 41)

etiquetaCostoPostre = Label(panelCosto, text = 'Costo Postre',  font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaCostoPostre.grid(row=2, column=0)
textoCostoPostre = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableCostoPostre)
textoCostoPostre.grid(row=2 ,column = 1, padx = 41)

etiquetaSubTotal = Label(panelCosto, text = 'SubTotal' , font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaSubTotal.grid(row=0, column=3)
textoSubTotal = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableSubTotal)
textoSubTotal.grid(row=0 ,column = 4, padx = 41)

etiquetaImpuesto = Label(panelCosto, text = 'Impuesto',  font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaImpuesto.grid(row=1, column=3)
textoImpuesto = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableImpuesto)
textoImpuesto.grid(row=1 ,column = 4, padx = 41)

etiquetaTotal = Label(panelCosto, text = 'Total',  font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiquetaTotal.grid(row=2, column=3)
textoTotal = Entry(panelCosto, font=("Dosis", 12, "bold"), bd=1, width=10, state='readonly',textvariable=variableTotal)
textoTotal.grid(row=2 ,column = 4, padx = 41)

#Botones
botones = ['Total','Factura','Guardar','Resetear']
botonesCreados = []
columnas = 0
for i in botones:
    i = Button(panelBotones,text= i, font=("Dosis", 14, "bold"), fg='white',bg='azure4',bd=1,width=7)
    botonesCreados.append(i)
    i.grid(row=0, column=columnas)
    columnas+=1

botonesCreados[0].config(command=total)
botonesCreados[1].config(command=factura)
botonesCreados[2].config(command=guardarFactura)
botonesCreados[3].config(command=resetearPantalla)

#Area de Ricibo
textoRecibo = Text(panelRecibo, font=("Dosis", 12, "bold"), bd=1, width=42, height=10)
textoRecibo.grid(row=0, column=0)

#############################################
#                Calculadora
#############################################
pantallaCalculadora = Entry(panelCalculadora, font=("Dosis", 16, "bold"), width=32, bd=1)
pantallaCalculadora.grid(row=0, column=0, columnspan=4)

fila = 1
columna = 0

botonesCalculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','CE','0','=','/']
botonesGuardados = []
for i in botonesCalculadora:
    i = Button(panelCalculadora, text=i, font=("Dosis", 16, "bold"), fg='white', bg='azure4', bd=1, width=7)
    i.grid(row=fila, column=columna)

    botonesGuardados.append(i)


    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0


botonesGuardados[0].config(command=lambda : click_boton('7'))
botonesGuardados[1].config(command=lambda : click_boton('8'))
botonesGuardados[2].config(command=lambda : click_boton('9'))
botonesGuardados[3].config(command=lambda : click_boton('+'))
botonesGuardados[4].config(command=lambda : click_boton('4'))
botonesGuardados[5].config(command=lambda : click_boton('5'))
botonesGuardados[6].config(command=lambda : click_boton('6'))
botonesGuardados[7].config(command=lambda : click_boton('-'))
botonesGuardados[8].config(command=lambda : click_boton('1'))
botonesGuardados[9].config(command=lambda : click_boton('2'))
botonesGuardados[10].config(command=lambda : click_boton('3'))
botonesGuardados[11].config(command=lambda : click_boton('*'))
botonesGuardados[12].config(command=lambda : borrar())
botonesGuardados[13].config(command=lambda : click_boton('0'))
botonesGuardados[14].config(command=lambda : obtener_resultado())
botonesGuardados[15].config(command=lambda : click_boton('/'))




aplicacion.mainloop() #Evita que la pantalla se cierre

