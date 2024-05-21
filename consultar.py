from datos import *
from funciones import abrir_csv, RUTA

def opcion():
    num_prod = abrir_csv(RUTA)
    print ("*******************************************************")
    print ("Que desea?")
    id = input(">> ")
    try:
        opcion = num_prod[int(id)-1][id]
        print ("*******************************************************")
        return opcion
    except Exception:
        print ("opcion no valida")
        print ("*******************************************************")
def consultar():
    abrir_csv(RUTA)

    

