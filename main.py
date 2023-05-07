from claseconjunto import Conjunto

def main():
    a = Conjunto([1, 2, 3, 4])
    b = Conjunto([3, 6, 9])

    while True:
        print("1. Unión de dos conjuntos")
        print("2. Diferencia de dos conjuntos")
        print("3. Verificar si dos conjuntos son iguales")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print(f"A + B = {a + b}")
        elif opcion == 2:
            print(f"A - B = {a - b}")
        elif opcion == 3:
            if a == b:
                print("Los conjuntos A y B son iguales")
            else:
                print("Los conjuntos A y B no son iguales")
        elif opcion == 4:
            break
        else:
            print("Opción inválida")
if __name__ == "__main__":
    main()