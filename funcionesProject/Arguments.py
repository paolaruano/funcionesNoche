#ejemplo de argumento predeterminado

def my_funcion(country = "Colombia"):
    print("I am from "+country)

#Invocar la funcion
my_funcion("Sweden")
my_funcion("India")
my_funcion()
my_funcion("Brazil")

#Ejemplo de argumento arbitrario
def mostrarEstudiantes(*args):
    print("El estudiante: "+ args[2])

mostrarEstudiantes("Emil", "Tobias", "Linus")

#Ejemplo argumentos de palabra clave
def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: "+carro2)

mostrarCarros(carro1="BMW", carro3="Ferrari", carro2="Ford")

#Ejempos arbitrarios **kwargs
def mostrarCLiente(**kwargs):
    print("Su apellido es: "+kwargs["apellido"])

mostrarCLiente(nombre="Tobias", apellido="Refsnes")