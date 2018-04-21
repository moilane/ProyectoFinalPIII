def EscribirLista(lista):
        file=open('mipefil.txt','a+')
        file.write(lista+'\n')
        file.close()
        print('Archivo escrito')



def LeerArchivo():
    file=open('mipefil.txt','r')
    cabecera=['nombre','apellido','edad'] #llaves del diccionario
    dict1={}
    dict2={}
    numlinea = 0
    for linea in file.readlines():
        lista=linea.split(',')
        count=0
        for elemento in lista:
            dict1[cabecera[count]]=elemento
            count+=1
        dict2[numlinea] = dict1
        numlinea+=1

    return dict2





test=LeerArchivo()

print(test[0])