
import os
import time
from collections import OrderedDict

#El menu funciona bien y se guarda en el .txt, lo subo junto para que vean como funciona, pero aun se tiene que aplicar las funcionas en las opciones.
# y no se coloca el mensaje en si en la opcion, puede pobarlo cuando ejecuta el problema.
#y el loop, un error cuando el cliente no coloca bien la opcion y poner el ID del empleado y el precio que seria el monto
#el problema con el programa es la manera que se guarda el .txt, no se puede guarda normalmente ya que el terminal da un error por el string
# Este es el error:    
#  file.write(transaccion + '\n')
# TypeError: unsupported operand type(s) for +: 'dict' and 'str'
#En la cual lo tenia que se reemplazada con el codigo escrito abajo en la linea 96 respectivamente. 

def opcion_1():
    """Efectivo"""
    print("Seleccionaste Efectivo!\n")
    print("Porfavor ingrese la cantidad desada que quieres pagar:")


def opcion_2():
    """Tarjeta de Debito/Credito"""
    print("Seleccionaste Tarjeta de Debito/Credito!\n")
    print("Porfavor ingrese los 16 digitos de su tarjeta: ")
    print("Fecha de expiracion: ")

os.system('cls')

if __name__ == '__main__':
  transaccion = {}

def add_initials(nom, ape, time, id):
    add = {}

    add["time"] = time
    add["ID de Empleado"] = id
    add["nom"] = nom
    add["ape"] = ape
    
    transaccion[id] = add

os.system('cls')

def fractura():
    for id in transaccion:
        add = transaccion[id]
        print(add["time"], "\n", add["ID de Empleado"], "\n", add["nom"], "\n", add["ape"], "\n", "Forma de pago escogido: ", "Monto: ", "Pago: ")

print("¡Bienvenido a la pantalla de transacciones de Bomba iPlena! Porfavor siga las instrucciones para procesa su transaccion.\n")

def add2():
    id = input("Ingrese su ID de Empleado: ")
    n = input("Nombre: ")
    a = input("Apellido: ")
    t = time.strftime("%m/%d/%Y, %H:%M:%S")

    add_initials(n, a, t, id)

    fractura()
add2()  

os.system('cls')

salir = False
mensaje = ('Porfavor seleccione su metodo de pago para procesar su transaccion.')

    # menu = {'1' : opcion_1, '2' : opcion_2 }

menu = OrderedDict(
        [
            ('1', opcion_1),
            ('2', opcion_2),
        ]
    )

while not salir:
    print(mensaje)

    for funcion, opcion in menu.items():
        mensaje_final = '{}) {}'.format(funcion, opcion.__doc__)
        print(mensaje_final)
    
    respuesta = input('\nOpcion: ')
    salir = respuesta == '0'

    opcion = menu.get(respuesta, None)
    if opcion:
        opcion()

else:
    print("Gracias por su transaccion! Tenga un buen dia!")
            

ruta2 = '.vscode\\transaccion.txt'
file = open(ruta2,'a+')
file.write('transaccion = % s'%transaccion + '\n')
file.close()
print('Transaccion guardada en archivo')

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
