from datos import *
from consultar import opcion

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


def mostrar_pedidos (datos):
    print ("P e d i d o s")
    for i in range(len(datos["pedidos"])):
        print ("------------------------------------------------")
        print ("Name - ",datos["pedidos"][i]["name"])
        print ("Categoria - ",datos["pedidos"][i]["categoria"])
        print ("Producto - ",datos["pedidos"][i]["producto"])
        print ("Nombre producto - ",datos["pedidos"][i]["nombre"])
        print ("Precio - ",datos["pedidos"][i]["precio"])
        print ("Cantidad - ",datos["pedidos"][i]["cantidad"])
        print ("Total - ",datos["pedidos"][i]["total"])    
        print ("------------------------------------------------")

datos = cargar_datos(PEDIDOS)
def mostrar():
    mostrar_pedidos(datos)
    
def comprar(datos:dict):
    pedidos= {}
    pedidos:dict
    op = opcion()
    
    pedidos["name"]= input("Ingrese el nombre: ")
    pedidos["categoria"]= op[0]
    pedidos["producto"]= op[1]
    pedidos["nombre"]= op[2]
    pedidos["precio"]= int(op[3])
    cant = input("Ingrese la cantidad: ")
    pedidos["cantidad"]= int(cant)
    pedidos["total"]= pedidos["precio"]*pedidos["cantidad"]
    print ("Su total a pagar es: ",pedidos["total"])
    
    datos["pedidos"].append(pedidos)
    return datos
def compras():
    datos = cargar_datos(PEDIDOS)
    datos = comprar(datos)
    guardar_datos(datos,PEDIDOS)