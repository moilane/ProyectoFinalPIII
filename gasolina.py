def menu ():
    
galones = 3.785 #Galones por litro

a = 95
b = 90
c = diesel
TotalA,TotalB,TotalC = 0,0,0

#le colocas def menu con las condiciones que deseas realizar.
 
tipo = input('Que tipo de gasolina desea [a,b,c] d = fin:')
 
while tipo.upper() != 'D':
    litros = int(input('Cuantos litros desea:'))
    if tipo == 'a':
        TipoA = litros * a
        TotalA = TotalA + TipoA
        print(TotalA)
        gl = TipoA / galones
    elif tipo == 'b':
        TipoB = litros * b
        TotalB = TotalB + TipoB
        print(TotalB)
        gl = TipoB / galones
    elif tipo == 'c':
        TipoC = litros * c
        TotalC = TotalC + TipoC
        print(TotalC)
        gl = TipoC / galones
    tipo = input('Que tipo de gasolina desea [a,b,c] d = fin:')
 
print('\nTotal gasolina tipo A = %d Bs' %TotalA)
print('Total gasolina tipo B = %d Bs' %TotalB)
print('Total gasolina tipo C = %d Bs' %TotalC)
 
total = TotalA + TotalB + TotalC
 
print('Total recaudado = %d' %total)