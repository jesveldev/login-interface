from tkinter import *
from tkinter import messagebox

#----------------------- VARIABLES - INTERFAZ DE SEGURIDAD ----------------------:

ResCondi1=1
ResCondi2=6
condi_pos_botones=1

admin="admin0"
pass_admin="azrahiesaseti"

admin2="admin1"
pass_admin2="1234"

condicion_de_cierre=0

# ---------------------- VARIABLES - INTERFAZ PRINCIPAL ------------------------:

usuario_ingresado_1="Programador"
usuario_ingresado_2="Usuario"

# ---------------- DECLARACION DE LA INTERFAZ DE SEGURIDAD --------------------:

ventana=Tk()
ventana.title("Inicio de Sesión")
ventana.resizable(False,False)

#------------------ DECLARACIÓN DE LA INTERFAZ PRINCIPAL -----------------------:

ventana2=Toplevel()
ventana2.title("Interfaz Principal")
ventana2.config(width=800,height=500,bg="black",bd=10,relief="ridge")
ventana2.resizable(False,False)
ventana2.withdraw()

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#------------------------- CÓDIGO DE LA INTERFAZ PRINCIPAL ------------------------:
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#--------------------------- FUNCIONES DE LOS BOTONES ------------------------------:

def CerrarSesion():

	valor=messagebox.askquestion("Salir","¿Estás seguro de que deseas cerrar sesión?")

	if valor=="yes":

		ventana2.withdraw()
		ventana.deiconify()

def CerrarPrograma():

	valor=messagebox.askquestion("Salir","¿Estás seguro de que deseas salir?")

	if valor=="yes":

		ventana.destroy()

#--------------------------------------- BOTONES ------------------------------------------------:

botonCerrarSesion=Button(ventana2,text="Cerrar Sesión",bg="black",fg="white",font=("Georgia",10),bd=10,relief="ridge")
botonCerrarSesion.config(width=10,height=0,command=CerrarSesion)
botonCerrarSesion.place(x=20,y=400)

botonCerrarProg=Button(ventana2,text="Salir",bg="black",fg="white",font=("Georgia",10),bd=10,relief="ridge")
botonCerrarProg.config(width=10,height=0,command=CerrarPrograma)
botonCerrarProg.place(x=20,y=350)

# -------------------------------- ETIQUETAS --------------------------------------------------:

indicador_sesion=Label(ventana2,text=f"| SESIÓN ACTIVA | {usuario_ingresado_1} |",bg="black",fg="white",font=("Georgia",10))
indicador_sesion.place(x=5000,y=5000)

indicador_sesion_2=Label(ventana2,text=f"| SESIÓN ACTIVA | {usuario_ingresado_2} |",bg="black",fg="white",font=("Georgia",10))
indicador_sesion_2.place(x=5000,y=5000)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#------------------------- CÓDIGO DE LA INTERFAZ DE SEGURIDAD-----------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


# ----------------- FUNCIONES DE LOS COMANDOS DE LOS MENÚES --------------------:

def OpcionLog():

	messagebox.showinfo("Información de la Aplicación","Versión 1.0\n\nFecha de Creación: 12-02-2021\n\nUltima Edición: 14-02-2021")

def OpcionCreditos():

	messagebox.showinfo("Créditos del Desarrollo","Programador: Jesús E. Velásquez")

# --------------------- FUNCIONES DE LOS COMANDOS DE LOS SUB-MENÚES ----------------------:

# COLORES DE LA INTERFAZ:

# ResCondi1 indica cual es la resolución actual de la interfaz
# ResCondi2 indica cual es el color actual de la interfaz 

# Si ResCondi1 es igual a 1 significa que la resolución es 510x510
# Si ResCondi1 es igual a 2 significa que la resolución es 600x510
# Si ResCondi1 es igual a 3 significa que la resolución es 700x510

# Si ResCondi2 es igual a 1 significa que el color de la interfaz es Rojo
# Si ResCondi2 es igual a 2 significa que el color de la interfaz es Rojo Oscuro
# Si ResCondi2 es igual a 3 significa que el color de la interfaz es Azul
# Si ResCondi2 es igual a 4 significa que el color de la interfaz es Azul Oscuro
# Si ResCondi2 es igual a 5 significa que el color de la interfaz es Gris
# Si ResCondi2 es igual a 6 significa que el color de la interfaz es Gris Claro
# Si ResCondi2 es igual a 7 significa que el color de la interfaz es Amarillo
# Si ResCondi2 es igual a 8 significa que el color de la interfaz es Dorado
# Si ResCondi2 es igual a 9 significa que el color de la interfaz es Negro
# Si ResCondi2 es igual a 10 significa que el color de la interfaz es Púrpura

def ColorRojo(variacion):

	global ResCondi1
	global ResCondi2

	if variacion==1:

		ventana.config(bg="red")

		boton1.config(bg="red")
		boton2.config(bg="red")

		ResCondi2=1

		if ResCondi1==1:

			labeldib1.place(x=0,y=0)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)


		elif ResCondi1==2:

			labeldib1.place(x=45,y=0)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=95,y=0)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

	if variacion==2:

		ventana.config(bg="dark red")

		boton1.config(bg="dark red")
		boton2.config(bg="dark red")

		ResCondi2=2

		if ResCondi1==1:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=0,y=0)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==2:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=45,y=0)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=95,y=0)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

def ColorAzul(variacion):

	global ResCondi1
	global ResCondi2

	if variacion==1:

		ventana.config(bg="blue")

		boton1.config(bg="blue")
		boton2.config(bg="blue")

		ResCondi2=3

		if ResCondi1==1:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=0,y=0)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==2:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=45,y=0)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=95,y=0)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

	elif variacion==2:

		ventana.config(bg="dark blue")

		boton1.config(bg="dark blue")
		boton2.config(bg="dark blue")

		ResCondi2=4

		if ResCondi1==1:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=0,y=0)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==2:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=45,y=0)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=95,y=0)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

def ColorAmarillo():

	global ResCondi1
	global ResCondi2

	ventana.config(bg="yellow")

	boton1.config(bg="yellow")
	boton2.config(bg="yellow")

	ResCondi2=5

	if ResCondi1==1:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=0,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=45,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=95,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

def ColorNegro():

	global ResCondi1
	global ResCondi2

	ventana.config(bg="black")

	boton1.config(bg="black")
	boton2.config(bg="black")

	ResCondi2=6

	if ResCondi1==1:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=0,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=45,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=95,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)


def ColorGris(variacion):

	global ResCondi1
	global ResCondi2

	if variacion==1:

		ventana.config(bg="gray")

		boton1.config(bg="gray")
		boton2.config(bg="gray")

		ResCondi2=7

		if ResCondi1==1:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=0,y=0)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==2:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=45,y=0)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=95,y=0)
			labeldib8.place(x=1000,y=1000)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

	elif variacion==2:

		ventana.config(bg="dark gray")

		boton1.config(bg="dark gray")
		boton2.config(bg="dark gray")

		ResCondi2=8

		if ResCondi1==1:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=0,y=0)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==2:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=45,y=0)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

		elif ResCondi1==3:

			labeldib1.place(x=1000,y=1000)
			labeldib2.place(x=1000,y=1000)
			labeldib3.place(x=1000,y=1000)
			labeldib4.place(x=1000,y=1000)
			labeldib5.place(x=1000,y=1000)
			labeldib6.place(x=1000,y=1000)
			labeldib7.place(x=1000,y=1000)
			labeldib8.place(x=95,y=0)
			labeldib9.place(x=1000,y=1000)
			labeldib10.place(x=1000,y=1000)

def ColorDorado():

	global ResCondi1
	global ResCondi2

	ventana.config(bg="gold")

	boton1.config(bg="gold")
	boton2.config(bg="gold")

	ResCondi2=9

	if ResCondi1==1:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=0,y=0)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=45,y=0)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi1==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=95,y=0)
		labeldib10.place(x=1000,y=1000)


def ColorPurpura():

	global ResCondi1
	global ResCondi2

	ventana.config(bg="purple")

	boton1.config(bg="purple")
	boton2.config(bg="purple")

	ResCondi2=10

	if ResCondi1==1:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=0,y=0)

	if ResCondi1==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=45,y=0)

	if ResCondi1==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=95,y=0)

# RESOLUCION DE LA INTERFAZ:

def Res1():

	global ResCondi1
	global ResCondi2

	global condi_pos_botones

	ResCondi1=1

	ventana.config(width=510,height=510)

	usuario.place(x=135,y=200)
	contrasenha.place(x=135,y=265)

	if condi_pos_botones==1:

		boton1.place(x=96,y=400)
		boton2.place(x=301,y=400)

	elif condi_pos_botones==2:

		boton1.place(x=195,y=320)
		boton2.place(x=195,y=380)

	if ResCondi2==1:

		labeldib1.place(x=0,y=0)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=0,y=0)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=0,y=0)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==4:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=0,y=0)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==5:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=0,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==6:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=0,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==7:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=0,y=0)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==8:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=0,y=0)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==9:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=0,y=0)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==10:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=0,y=0)

def Res2():

	global ResCondi1
	global ResCondi2

	ResCondi1=2

	usuario.place(x=180,y=200)
	contrasenha.place(x=180,y=265)

	if condi_pos_botones==1:

		boton1.place(x=136,y=400)
		boton2.place(x=351,y=400)

	elif condi_pos_botones==2:

		boton1.place(x=242,y=320)
		boton2.place(x=242,y=380)

	ventana.config(width=600,height=510)

	if ResCondi2==1:

		labeldib1.place(x=45,y=0)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=45,y=0)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=45,y=0)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==4:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=45,y=0)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==5:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=45,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==6:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=45,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==7:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=45,y=0)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==8:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=45,y=0)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==9:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=45,y=0)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==10:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=45,y=0)

def Res3():

	global ResCondi1
	global ResCondi2

	ResCondi1=3

	ventana.config(width=700,height=510)

	usuario.place(x=230,y=200)
	contrasenha.place(x=230,y=265)

	if condi_pos_botones==1:

		boton1.place(x=181,y=400)
		boton2.place(x=401,y=400)

	elif condi_pos_botones==2:

		boton1.place(x=292,y=320)
		boton2.place(x=292,y=380)

	if ResCondi2==1:

		labeldib1.place(x=95,y=0)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==2:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=95,y=0)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==3:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=95,y=0)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==4:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=95,y=0)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==5:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=95,y=0)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==6:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=95,y=0)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==7:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=95,y=0)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==8:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=95,y=0)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==9:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=190,y=0)
		labeldib10.place(x=1000,y=1000)

	elif ResCondi2==10:

		labeldib1.place(x=1000,y=1000)
		labeldib2.place(x=1000,y=1000)
		labeldib3.place(x=1000,y=1000)
		labeldib4.place(x=1000,y=1000)
		labeldib5.place(x=1000,y=1000)
		labeldib6.place(x=1000,y=1000)
		labeldib7.place(x=1000,y=1000)
		labeldib8.place(x=1000,y=1000)
		labeldib9.place(x=1000,y=1000)
		labeldib10.place(x=95,y=0)

# TIPOS DE TEXTURA DE LA INTERFAZ:

def DisFlat():

	ventana.config(relief="flat")

def DisGroove():

	ventana.config(relief="groove")

	boton1.config(relief="groove")
	boton2.config(relief="groove")

def DisSunken():

	ventana.config(relief="sunken")

	boton1.config(relief="sunken")
	boton2.config(relief="sunken")

def DisRidge():

	ventana.config(relief="ridge")

	boton1.config(relief="ridge")
	boton2.config(relief="ridge")

def DisRaised():

	ventana.config(relief="raised")

	boton1.config(relief="raised")
	boton2.config(relief="raised")

# TIPOS DE CURSORES EN LA INTERFAZ:

def CursorCross():

	ventana.config(cursor="cross")

def CursorPirate():

	ventana.config(cursor="pirate")

def CursorHand2():

	ventana.config(cursor="hand2")

# POSICIÓN DE LOS BOTONES: 

def Posicion1():

	global condi_pos_botones

	condi_pos_botones=1

	if ResCondi1==1:

		boton1.place(x=96,y=400)
		boton2.place(x=301,y=400)

	elif ResCondi1==2:

		boton1.place(x=136,y=400)
		boton2.place(x=351,y=400)

	elif ResCondi1==3:

		boton1.place(x=181,y=400)
		boton2.place(x=401,y=400)

def Posicion2():

	global condi_pos_botones

	condi_pos_botones=2

	if ResCondi1==1:

		boton1.place(x=195,y=320)
		boton2.place(x=195,y=380)

	elif ResCondi1==2:
		
		boton1.place(x=242,y=320)
		boton2.place(x=242,y=380)

	elif ResCondi1==3:

		boton1.place(x=292,y=320)
		boton2.place(x=292,y=380)


# FUNCIONES DE INICIO DE SESIÓN:

recolector_de_texto=StringVar()
recolector_de_texto2=StringVar()

def LimpiarCampos():

	recolector_de_texto.set("")
	recolector_de_texto2.set("")

def IniciarSesion():

	global admin
	global pass_admin
	global condicion_de_cierre

	comprobar_usuario= recolector_de_texto.get()
	comprobar_pass= recolector_de_texto2.get()

	if comprobar_usuario=="" or comprobar_pass=="":

		messagebox.showinfo("Error de Inicio de Sesión","Debes llenar los campos para poder iniciar sesión.")

	else:

		if comprobar_usuario==admin:

			if comprobar_pass==pass_admin:

				indicador_sesion.place(x=5,y=5)
				indicador_sesion_2.place(x=5000,y=5000)

				recolector_de_texto.set("")
				recolector_de_texto2.set("")

				ventana.withdraw()
				ventana2.deiconify()

			else:

				if condicion_de_cierre!=3:

					messagebox.showinfo("Error de Inicio de Sesión","La contraseña que ha ingresado es incorrecta.")
					condicion_de_cierre+=1

		elif comprobar_usuario==admin2:

			if comprobar_pass==pass_admin2:

				indicador_sesion_2.place(x=5,y=5)
				indicador_sesion.place(x=5000,y=5000)

				recolector_de_texto.set("")
				recolector_de_texto2.set("")
				
				ventana.withdraw()
				ventana2.deiconify()

			else:

				if condicion_de_cierre!=3:

					messagebox.showinfo("Error de Inicio de Sesión","La contraseña que ha ingresado es incorrecta.")
					condicion_de_cierre+=1


		else:

			messagebox.showinfo("Error de Inicio de Sesión","El nombre de usuario ingresado es incorrecto.")
			condicion_de_cierre+=1

	if condicion_de_cierre==3:

		sys.exit()

# ------------------- BARRA MENÚ -------------------------:

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu,cursor="cross", relief="ridge", bd=15, bg="black",width=510,height=510)

# ---------------- DIBUJO DEL FONDO --------------------------:

dib1=PhotoImage(file="imagenes/rojo1.png")
dib2=PhotoImage(file="imagenes/rojo2.png")
dib3=PhotoImage(file="imagenes/azul1.png")
dib4=PhotoImage(file="imagenes/azul2.png")
dib5=PhotoImage(file="imagenes/amarillo.png")
dib6=PhotoImage(file="imagenes/negro.png")
dib7=PhotoImage(file="imagenes/gris1.png")
dib8=PhotoImage(file="imagenes/gris2.png")
dib9=PhotoImage(file="imagenes/dorado.png")
dib10=PhotoImage(file="imagenes/purpura.png")

labeldib1=Label(ventana,image=dib1,bg="red")
labeldib2=Label(ventana,image=dib2,bg="dark red")
labeldib3=Label(ventana,image=dib3,bg="blue")
labeldib4=Label(ventana,image=dib4,bg="dark blue")
labeldib5=Label(ventana,image=dib5,bg="yellow")
labeldib6=Label(ventana,image=dib6,bg="black")
labeldib7=Label(ventana,image=dib7,bg="gray")
labeldib8=Label(ventana,image=dib8,bg="dark gray")
labeldib9=Label(ventana,image=dib9,bg="gold")
labeldib10=Label(ventana,image=dib10,bg="purple")

labeldib1.place(x=1000,y=1000)
labeldib2.place(x=1000,y=1000)
labeldib3.place(x=1000,y=1000)
labeldib4.place(x=1000,y=1000)
labeldib5.place(x=1000,y=1000)
labeldib6.place(x=0,y=0)
labeldib7.place(x=1000,y=1000)
labeldib8.place(x=1000,y=1000)
labeldib9.place(x=1000,y=1000)
labeldib10.place(x=1000,y=1000)

#----------------------- ENTRADAS DE TEXTO --------------------:

usuario=Entry(ventana,bg="gray",fg="white",font=("Georgia",13),justify="center",show="*",textvariable=recolector_de_texto)
contrasenha=Entry(ventana,bg="gray",fg="white",font=("Georgia",13),justify="center",show="*",textvariable=recolector_de_texto2)

usuario.place(x=135,y=200)
contrasenha.place(x=135,y=265)

# -------------------- BOTONES DE LA INTERFAZ ------------------:

boton1=Button(ventana,bg="black",bd=3,fg="white",text="Entrar",width=9,height=1,font=("Georgia",10),command=IniciarSesion,relief="ridge")
boton2=Button(ventana,bg="black",bd=3,fg="white",text="Limpiar",width=9,height=1,font=("Georgia",10),command=LimpiarCampos,relief="ridge")

boton1.place(x=96,y=400)
boton2.place(x=301,y=400)

# ------------------- ELEMENTOS DE LA BARRA MENÚ ---------------:

menu_edicion=Menu(barraMenu,tearoff=0)
menu_opciones=Menu(barraMenu,tearoff=0)
menu_acercade=Menu(barraMenu,tearoff=0)

barraMenu.add_cascade(label="Opciones",menu=menu_opciones)
barraMenu.add_cascade(label="Edicion",menu=menu_edicion)
barraMenu.add_cascade(label="Acerca de",menu=menu_acercade)

# ------------------- SUB-MENÚES DE LOS ELEMENTOS DE LA BARRA -----------:

submenu_color=Menu(barraMenu,tearoff=0)
submenu_resolucion=Menu(barraMenu,tearoff=0)
submenu_disenho=Menu(barraMenu,tearoff=0)
submenu_cursor=Menu(barraMenu,tearoff=0)
submenu_posbotones=Menu(barraMenu,tearoff=0)

menu_edicion.add_cascade(label="Resolución",menu=submenu_resolucion)
menu_edicion.add_cascade(label="Color de Fondo",menu=submenu_color)
menu_edicion.add_cascade(label="Diseño",menu=submenu_disenho)

menu_opciones.add_cascade(label="Cursor",menu=submenu_cursor)
menu_opciones.add_cascade(label="Pos. Botones",menu=submenu_posbotones)

# ------------------- COMANDOS DE LOS MENÚES DE LA BARRA ----------------:

menu_acercade.add_command(label="Créditos",command=OpcionCreditos)
menu_acercade.add_separator()
menu_acercade.add_command(label="Log",command=OpcionLog)

# ------------------- COMANDOS DE LOS SUB-MENUES ----------------------:

submenu_resolucion.add_command(label="510x510",command=Res1)
submenu_resolucion.add_separator()
submenu_resolucion.add_command(label="600x510",command=Res2)
submenu_resolucion.add_separator()
submenu_resolucion.add_command(label="700x510",command=Res3)

submenu_color.add_command(label="Rojo",command=lambda:ColorRojo(1))
submenu_color.add_command(label="Rojo Oscuro",command=lambda:ColorRojo(2))
submenu_color.add_separator()
submenu_color.add_command(label="Azul",command=lambda:ColorAzul(1))
submenu_color.add_command(label="Azul Oscuro",command=lambda:ColorAzul(2))
submenu_color.add_separator()
submenu_color.add_command(label="Gris",command=lambda:ColorGris(1))
submenu_color.add_command(label="Gris Claro",command=lambda:ColorGris(2))
submenu_color.add_separator()
submenu_color.add_command(label="Amarillo",command=ColorAmarillo)
submenu_color.add_command(label="Negro",command=ColorNegro)
submenu_color.add_command(label="Dorado",command=ColorDorado)
submenu_color.add_command(label="Púrpura",command=ColorPurpura)

submenu_disenho.add_command(label="Flat",command=DisFlat)
submenu_disenho.add_command(label="Sunken",command=DisSunken)
submenu_disenho.add_command(label="Groove",command=DisGroove)
submenu_disenho.add_command(label="Raised",command=DisRaised)
submenu_disenho.add_command(label="Ridge",command=DisRidge)

submenu_cursor.add_command(label="Cross",command=CursorCross)
submenu_cursor.add_command(label="Hand 2",command=CursorHand2)
submenu_cursor.add_command(label="Pirate",command=CursorPirate)

submenu_posbotones.add_command(label="Costados",command=Posicion1)
submenu_posbotones.add_command(label="Centro",command=Posicion2)

# ----------------------- MAINLOOP DE LA INTERFAZ DE SEGURIDAD ----------------------------:

ventana.mainloop()


