from Areas import *
from Distancias import *
from Volumenes import *

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
                print(f'El area del triangulo es: {areaTriangulo.areaTriangulo():.2f}')
            elif opA == 2:
                valor1 = float(input('Ingrese base: '))
                valor2 = float(input('Ingrese altura: '))

                areaRectangulo = AreaRectangulo(valor1, valor2)
                print(f'El area del rectangulo es: {areaRectangulo.areaRectangulo():.2f}')
            elif opA == 3:
                valor1 = float(input('Ingrese valor de diagonal mayor: '))
                valor2 = float(input('Ingrese valor de diagonal menor: '))

                areaRombo = AreaRombo(valor1, valor2)
                print(f'El area del rombo es: {areaRombo.areaRombo():.2f}')
            elif opA == 4:
                valor1 = float(input('Ingrese valor de lado 1: '))
                valor2 = float(input('Ingrese valor de lado 2: '))

                areaCuadrado = AreaCuadrado(valor1, valor2)
                print(f'El area del cuadrado es: {areaCuadrado.areaCuadrado():.2f}')
            else:
                print('Opcion incorrecta, intente de nuevo...')

        elif opcion == 2:
            print('Volumenes'.center(50,'*'))
            print('1- Cuadrado')
            print('2- Rectangulo')
            print('3- Triangulo')
            print('4- Circulo')

            opV = int(input('Ingrese la figura a calcular: '))

            if opV == 1:
                valor1 = float(input('Ingrese lado: '))

                volumenCuadrado = VolumenCuadrado(valor1)
                print(f'El volumen del cuadrado es: {volumenCuadrado.Volumencuadrado():.2f}')
            elif opV == 2:
                valor1 = float(input('Ingrese largo: '))
                valor2 = float(input('Ingrese ancho: '))
                valor3 = float(input('Ingrese altura: '))

                volumenRectangulo = VolumenRectangulo(valor1, valor2, valor3)
                print(f'El volumen del rectangulo es: {volumenRectangulo.Volumenrectangulo():.2f}')
            elif opV == 3:
                valor1 = float(input('Ingrese altura: '))
                valor2 = float(input('Ingrese base: '))
                valor3 = float(input('Ingrese largo: '))

                volumenTriangulo = VolumenTriangulo(valor1, valor2, valor3)
                print(f'El volumen del triangulo es: {volumenTriangulo.Volumentriangulo():.2f}')
            elif opV == 4:
                valor1 = float(input('Ingrese el radio: '))
                pi = 3.1416

                volumenCirculo = VolumenCirculo(valor1, pi)
                print(f'El volumen del circulo es: {volumenCirculo.Volumencirculo():.2f}')

        elif opcion == 3:
            print('Distancias'.center(50,'*'))
            print('1- Cuadrado')
            print('2- Rectangulo')
            print('3- Triangulo')
            print('4- Circulo')

            opD = int(input('Ingrese la figura a calcular: '))

            if opD == 1:
                valor1 = float(input('Ingrese valor de lado: '))

                distanciaCuadrado = DistanciaCuadrado(valor1)
                print(f'La distancia del cuadrado es: {distanciaCuadrado.distanciaCuadrado():.2f}')
            elif opD == 2:
                valor1 = float(input('Ingrese valor de base: '))
                valor2 = float(input('Ingrese valor de altura: '))

                distanciaRectangulo = DistanciaRectangulo(valor1, valor2)
                print(f'La distancia del rectangulo es: {distanciaRectangulo.distanciaRectangulo():.2f}')
            elif opD == 3:
                valor1 = float(input('Ingrese valor de lado: '))

                distanciaTriangulo = DistanciaTriangulo(valor1)
                print(f'La distancia del triangulo es: {distanciaTriangulo.distanciaTriangulo():.2f}')
            elif opD == 4:
                valor1 = float(input('Ingrese valor de diametro: '))
                pi = 3.1416

                distanciaCirculo = DistanciaCirculo(valor1,pi)
                print(f'La distancia del circulo es: {distanciaCirculo.distanciaCirculo():.3f}')

        elif opcion == 4:
            print("Saliste del programa...","\U0001F614")
        else:
            print('Opcion incorrecta, intente de nuevo...')

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
