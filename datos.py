import json

def cargar_datos(archivo):
    datos:dict
    with open(archivo, "r", encoding='utf-8') as file:
        datos = json.load(file)
    return datos

        
        

def guardar_datos(datos:dict, archivo):
    diccionario = json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()

TIENDA ="json/tienda.json"
PEDIDOS = "json/pedidos.json"


        