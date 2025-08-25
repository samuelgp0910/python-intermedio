import os
archivo_contactos = "contactos.txt"
def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    correo = input("Ingrese el correo: ")
    
    with open(archivo_contactos, "a") as f:
        f.write(f"{nombre},{telefono},{correo}\n")
    print("Contacto agregado correctamente")

def listar_contactos():
    if not os.path.exists(archivo_contactos):
        print("No hay contactos guardados")
        return
        
    with open(archivo_contactos, "r") as f:
        lineas = f.readlines()
    if not lineas:
        print("No hay contactos guardados")
        return
        
    print("\nLista de contactos:")
    for i, linea in enumerate(lineas, 1):
        datos = linea.strip().split(",")
        if len(datos) == 3:
            print(f"{i}. {datos[0]} - {datos[1]} - {datos[2]}")

def buscar_contacto():
    if not os.path.exists(archivo_contactos):
        print("No hay contactos guardados")
        return
        
    termino = input("Ingrese nombre o correo a buscar: ").lower()
    encontrados = False
    with open(archivo_contactos, "r") as f:
        for linea in f:
            if termino in linea.lower():
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    print(f"{datos[0]} | {datos[1]} | {datos[2]}")
                    encontrados = True                  
    if not encontrados:
        print("No se encontraron contactos")

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Salir")      
        opcion = input("Seleccione una opcion: ")        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            listar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    main()