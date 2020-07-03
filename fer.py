f=open("archivo.txt","r")
delimitador=str("-")
lista=['Hola','Adios','Hoy']

linea = f.readline()
aImprimir = ""
primera = True

while linea != "":
    palabras = linea.split(" ")
    print (linea.split())

   
    print (aImprimir)

   



    for palabra in palabras:
        for clave in lista:
            if clave == palabra:
                if primera:
                    aImprimir+=clave
                    primera = False

                else:
                    aImprimir+=delimitador+clave

    linea = f.readline()

print(aImprimir)

