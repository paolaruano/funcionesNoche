#Ejemplo para crear el area del triangulo

#Entradas
base = int(input("Ingrese la base del triangulo "))
altura = int(input("Ingrese la altura del triangulo "))

#Proceso
def calcularAreaTriangulo(b,a):
    area =(b*a)/2
    #print("El area del triangulo es: ", area)
    return area

resultado = calcularAreaTriangulo(base,altura) +4
print("El area del triangulo es: ", resultado)