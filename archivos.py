def notas():
    with open("notas.txt", "a") as archivo:
        while True:
            nota = input("Escribe una nota (o 'salir' para terminar): ")
            if nota.lower() == 'salir':
                break
            archivo.write(nota + "\n")
    print("Notas guardadas en notas.txt")
notas ()