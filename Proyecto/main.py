from areas import AreaTriangulo

opcion = None

print("Escoja las opciones a continuacion...")
print("1- Areas")
print("2- Volumenes")
print("3- Distancias")
print("4- Salir")

opcion = int(input("Selecciona una opcion: "))

while opcion != 4:

    if opcion == 1:
        print("Areas".center(50,'*'))

        valor1 = float(input("Ingrese base: "))
        valor2 = float(input("Ingrese altura: "))

        area = AreaTriangulo(valor1, valor2)

        print(f"El area del cuadrado es: {area.areaTriangulo()}")

