
import os
import time

transaccion = {}

def add_initials(nom, ape):
    add = {}

    add["nom"] = nom
    add["ape"] = ape

    transaccion[nom] = add

def fractura():
    for nom in transaccion:
        add = transaccion[nom]
        print(time.strftime("%c"), "\n", add["nom"], "\n", add["ape"], "\n", "Forma de pago escogido: ", "Monto: ", "Pago: ")

def add2():
    n = input("Nombre: ")
    a = input("Apellido: ")

    add_initials(n, a)

    fractura()

add2()


ruta2 = '.vscode\\transaccion.txt'
file = open(ruta2,'a+')
file.write('transaccion = % s'%transaccion + '\n')
file.close()
print('Archivo escrito')

# print('¡Bienvenido a la pantalla de transacciones de Bomba iPlena! Porfavor siga las instrucciones para procesa su transaccion.')
    
# #un codigo acerca del empleado conectado antediendo el cliente

# nom = input("Nombre: ")
# ape = input("Apellido: ")

# opcion = input("Porfavor escoga su metodo de pago: \n\n1 - Efectivo \n2 - Tarjeta de debito \n3 - Tarjeta de credito \n\nOpcion:")

# os.system('cls')

# #hace el menu como un diccionario, definir la opcion y retornarlo.

# if opcion=="1":
#     print("Escogiste a pagar en efectivo!")
#     ecf = input("Cuanto deseas pagar?: ")
#     #colocar el producto y si pago de mas ponga la resta a la cantidad que se devuelve
# elif opcion=="2":
#     print("Escogiste a pagar en Tarjeta de debito!")
#     deb = input("Coloque los 16 digitos de su tarjeta: ") #poner un error cuando no coloca los 16 numeros
#     fecha = input("Coloque la fecha de expiracion: ") #error cuando no pone una fecha de expiracion
# elif opcion=="3":
#     print("Escogiste a pagar en Tarjeta de debito!")
#     cred = input("Coloque los 16 digitos de su tarjeta: ")
#     fecha2 = input("Coloque la fecha de expiracion: ")
# else:
#     print("opcion invalido, porfavor escoga una opcion presentado.")
    
#poner el loop del menu cuando coloca una opcion de error.
#registracion de lo datos al final que imprime la factura.
#guadar en .txt los datos de la transaccion.
#retorna los valores que la persona ingrese    