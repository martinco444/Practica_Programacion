# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# La función recibirá por parámetro sólo UN polígono a la vez.
# Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# Imprime el cálculo del área de un polígono de cada tipo.


def Calculo_Area_poligono():
    print("Ingresa el poligono al que deseas calcular el area") 
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")

    val_res = input()

    if (val_res == "1"):
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print("el area del triangulo es: ", area)
    elif (val_res == "2"):
        lado = float(input("Ingresa la dimension del lado de cuadrado: "))
        area = lado * lado
        print("el area del cuadrado es: ", area, "cm²")
    elif (val_res == "3"):
        base = float(input("Ingresa la base del rectángulo: ")) 
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura
        print("el area del rectángulo es: ", area)

Calculo_Area_poligono()