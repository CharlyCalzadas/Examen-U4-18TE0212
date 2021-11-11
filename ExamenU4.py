"""
En este archivo se desarrollaran todas las clases para el escenario propuesto
"""

#CLASES ORIENTADAS AL MANEJO DE ERRORES
class misErrores(Exception):
    """Clase base para las excepciones de este modulo."""
    pass

class RangoError(misErrores):
    """Este error es propio"""
    def __init__(self, expression):
        self.expression = expression



#CLASES ORIENTADAS AL SUJETO
class Persona:

    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,carrera=None,energia=10):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__credito = saldoCuenta
        self.__nacimiento = fechaNacimiento
        self.__estudios = estudios
        self.__carrera = carrera
        self.__energia = energia
        self.__guardaropa = []
        self.__alacena = []


    def vestir(self):
        pass

    def comprar(self):
        pass


    def dormir(self):
        print("Es hora de dormir, ha sido un dia muy largo...")
        #Solicitaremos las horas para dormir
        while True:
            try:
                horas = float(input("¿Cuantas horas dormiremos? (Maximo podemos dormir 10 hrs): "))
                if ((horas<0) & (horas>10)):
                    raise RangoError("RangoError")
                else:
                    break

            except RangoError:
                print(self.__nombre," recuerda que solo podemos dormir de 1 a 10 horas")

            except ValueError:
                print(self.__nombre," el valor que ingresaste no es totalmente numerico")

        self.__energia = self.__energia + (horas * 1)

    def obtenerEstado(self):
        print("Actualmente : ",self.__nombre, "se encuentra:")
        print("Energia:         ",self.__energia)
        print("Saldo en cuenta: ", self.__credito)


    def comer(self):
        pass

    def comprar(self):
        pass


class Empleado(Persona):
    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,carrera=None,energia=10,):
        super().__init__(nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,carrera,energia)
