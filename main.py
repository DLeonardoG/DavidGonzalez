from importaciones import *

def main():
    while True:
        print ("*********************************************************")
        print (" 0. Salir \n 1. Registrarse \n 2. Consultar\n 3. Comprar\n 4. Mostrar pedidios")
        op = input("ingrese una opcion: \n>> ")
        if op == "1": registro()
        elif op == "2": consultar()
        elif op == "3": compras()
        elif op == "4": mostrar()
        elif op == "0": 
            while True:
                print ("Seguro que desea salir? \n 1. Si \n 2. No")
                op = input("ingrese una opcion: \n>> ")
                if op == "1": return print ("Chaooo...")
                elif op == "2": 
                    print("Continuemos...")
                    break
                else: print ("Opcion no valida")
        else: print ("Opcion no valida")
main()