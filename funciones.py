from datetime import datetime
import csv

def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha
fecha = time_now()

def reportar_venta_a_txt():
    ruta_errores = ("practice/txt/errrores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_venta = f"{fecha}: venta" 
        f.write(mensaje_venta + '\n')
        
def reportar_venta():
    ruta_errores = ("practice/txt/errrores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_venta = f"{fecha}: opcion de menu no valida..." 
        f.write(mensaje_venta + '\n')
        
RUTA = "cvs/catalogo.csv"
def abrir_csv(archivo):
    with open(archivo, 'r') as file:
        read = csv.reader(file, delimiter=",")
        read:dict
        count = 0
        num_prod = []
        
        for re in read: 
            lista=[]
            print("----------------------------------------------------------------")
            count += 1
            print(count,". : ")
            print(".................................................................")
            for line in re:
                print(line.strip())
                lista.append(line.strip())
            producto = {str(count) :lista}
            num_prod.append(producto)
            
        
        #print (num_prod)
        return num_prod


