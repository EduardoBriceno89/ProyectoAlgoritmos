from areas import *

opcion = None

while opcion != 4:

    try:
        print('Opciones'.center(50,'*'))
        print('1- Areas')
        print('2- Volumenes')
        print('3- Distancias')
        print('4- Salir')

        opcion = int(input('Ingrese opcion: '))

        if opcion == 1:
            print('Areas'.center(50,'*'))
            print('1- Triangulo')
            print('2- Rectangulo')
            print('3- Rombo')
            print('4- Cuadrado')

            opA = int(input('Ingrese la figura a calcular: '))

            if opA == 1:
                valor1 = float(input('Ingrese base: '))
                valor2 = float(input('Ingrese Altura: '))

                areaTriangulo = AreaTriangulo(valor1, valor2)
                print(f'El area del triangulo es: {areaTriangulo.areaTriangulo()}')
            elif opA == 2:
                valor1 = float(input('Ingrese base: '))
                valor2 = float(input('Ingrese altura: '))

                areaRectangulo = AreaRectangulo(valor1, valor2)
                print(f'El area del rectangulo es: {areaRectangulo.areaRectangulo()}')
            elif opA == 3:
                valor1 = float(input('Ingrese valor de diagonal mayor: '))
                valor2 = float(input('Ingrese valor de diagonal menor: '))

                areaRombo = AreaRombo(valor1, valor2)
                print(f'El area del rombo es: {areaRombo.areaRombo()}')
            elif opA == 4:
                valor1 = float(input('Ingrese valor de lado 1: '))
                valor2 = float(input('Ingrese valor de lado 2: '))

                areaCuadrado = AreaCuadrado(valor1, valor2)
                print(f'El area del cuadrado es: {areaCuadrado.areaCuadrado()}')
            else:
                print('Opcion incorrecta, intente de nuevo...')

        elif opcion == 2:
            print('Volumenes'.center(50,'*'))
        elif opcion == 3:
            print('Distancias'.center(50,'*'))
            print('1- Triangulo')
            print('2- Cuadrado')
            print('3- Rombo')
        else:
            print('Opcion incorrecta, intente de nuevo...')

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del programa')
