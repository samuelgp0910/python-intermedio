def dividir():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = num1 / num2
        print(f"El resultado de {num1} ÷ {num2} = {resultado}")
        
    except ValueError:
        print("Error: Debe ingresar números válidos")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    dividir()     