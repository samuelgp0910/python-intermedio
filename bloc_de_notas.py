def notas():
    while True:
        opcion = input("\n1. Agregar\n2. Borrar\n3. Salir\nOpción: ")
        
        if opcion == '1':
            with open("notas.txt", "a") as f:
                while True:
                    nota = input("Nota (salir para terminar): ")
                    if nota.lower() == 'salir': break
                    f.write(nota + "\n")
            print("Notas guardadas")
            
        elif opcion == '2':
            try:
                with open("notas.txt", "r") as f:
                    notas = f.readlines()
                
                if not notas:
                    print("No hay notas")
                    continue
                
                for i, n in enumerate(notas, 1):
                    print(f"{i}. {n.strip()}")
                
                num = int(input("Número a borrar (0 cancela): "))
                if num == 0: continue
                
                if 1 <= num <= len(notas):
                    del notas[num-1]
                    with open("notas.txt", "w") as f:
                        f.writelines(notas)
                    print("Nota borrada")
                    
            except: print("No hay notas")
                
        elif opcion == '3':
            print("¡Adiós!")
            break

notas() 