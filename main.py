import json

productos = []

try:
    with open("datos.json","r") as archivo:
        productos = json.load(archivo)

except FileNotFoundError:
    with open("datos.json","w") as archivo:
        productos = []


def actualizar():
    with open("datos.json","w") as archivo:
        json.dump(productos,archivo)


while True:
    opciones = input("\nA - agregar\nR - Remover\nL - Listar\nS - Salir\n")
    
    match opciones:
        case "S":
            break
        case "A":
            prod = input("\nProducto: ")
            precio = float(input("\nPrecio: "))
            categoria = input("\nCategoria: ")
            
            elProducto = [prod,precio,categoria]
            productos.append(elProducto)
            
            actualizar()
            
        case "R":
            quitar = input("\nProducto a remover: ").strip()
            productos.remove(quitar)
            
            actualizar()
            
        case "L":
            print(productos)
            

