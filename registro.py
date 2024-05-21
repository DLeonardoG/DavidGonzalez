from datos import *

datos = cargar_datos(TIENDA)


def registrar(datos:dict):
    clientes={}
    cedula = str(input("Ingrese su cedula: "))
    
    for i in range(len(datos["clientes"])):
        if datos["clientes"][i]["cedula"] == cedula:
            print (datos["clientes"][i]["cedula"],"ya se encuentra registrado :")
            return datos
    nombre = input("Ingrese su nombre: ")
    clientes["cedula"]= cedula
    clientes["nombre"]= nombre

    clientes["ciudad"]=input("Ingrese la ciudad: ")
    clientes["direccion"]=input("Ingrese la direccion: ")
    clientes["email"]=input("Ingrese el email: ")
     
    datos["clientes"].append(clientes)
    print ("Registro exitoso")
    return datos

def registro():
    datos = cargar_datos(TIENDA)
    datos = registrar(datos)
    guardar_datos(datos,TIENDA)





