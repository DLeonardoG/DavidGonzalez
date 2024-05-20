from datos import *
from funciones import abrir_csv, RUTA


menu = abrir_csv(RUTA)
print ("*******************************************************")
print ("Que desea?")
print ("*******************************************************")



def consult(datos):
    datos = dict(datos)
    for i in datos["productos"]:
        for j in i:
            print ("")
            
            print("id")
            print(j)
            print ("")
            print("tipo_producto")
            print(j)
            print ("")
            print("clase")
            print(j)
            print ("")
            print("precios")
            print(j)
            print ("")

        return datos

def consultar():
    datos = cargar_datos(TIENDA)
    datos = consult(datos)
    guardar_datos(datos, TIENDA)

