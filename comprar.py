
from datos import *

def agregar_producto(datos:dict):
    id =input("Ingrese el id del Producto: ")
    for i in datos["productos"]["base"]:
        if datos["productos"]["base"]["id"] == id:
            documento = input("Ingrese el documento: ")
            for j in range(len(datos["clientes"])):
                if datos["clientes"][j]["documento"] == documento:
                    datos:dict
                    ventas={}
                    ventas["id"]= datos["productos"][i]["id"]
                    datos["ventas"].append(ventas)
                    print("A ",ventas["nombre"]," se le añadio", ventas[i]," exitosamente")
                    return datos

def compras():
    datos = cargar_datos
    datos = agregar_producto(datos)
    guardar_datos(datos,TIENDA)