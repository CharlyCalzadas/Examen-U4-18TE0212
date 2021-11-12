"""
En este archivo se desarrollaran todas las clases para el escenario propuesto
"""

#CLASES ORIENTADAS AL MANEJO DE ERRORES -------------------------------------
class misErrores(Exception):
    """Clase base para las excepciones de este modulo."""
    pass

class RangoError(misErrores):
    """Este error es propio"""
    def __init__(self, expression):
        self.expression = expression



#CLASES ORIENTADAS AL SUJETO -------------------------------------
class Persona:

    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,telefono,carrera=None,energia=10):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__credito = float(saldoCuenta)
        self.__nacimiento = fechaNacimiento
        self.__estudios = estudios
        self.__carrera = carrera
        self.__telefono = telefono
        self.__energia = energia
        self.guardaropa = []
        self.alacena = []

    #Metodos para agregar productos al armario y alacena
    def addAlacena(self,objeto):
        self.alacena.append(objeto)

    def getAlacena(self):
        return self.alacena

    def addGuardaropa(self,objeto):
        self.guardaropa.append(objeto)

    def getGuardaropa(self):
        return self.guardaropa

    #Metodos comunes
    def mostrarGuardaropa(self):
        print("¿Que usaremos el dia de hoy?")
        j=0
        for prendas in self.guardaropa:
            print(j,".- ",prendas.printNombre(), "de caracteristicas: ",prendas.getDescripcion())
            j=j+1
        print("")

    def vestir(self,numP:int):
        print(self.__nombre, "esta usando: ",self.guardaropa[numP].printNombre(), "de caracteristicas: ",self.guardaropa[numP].getDescripcion())
        self.__energia = self.__energia - 0.1

    def mostrarAlacena(self):
        print("¿Desea consumir algo?")
        j=0
        for alimentos in self.alacena:
            print(j,".- ",alimentos.printNombre())
            j=j+1
        print("")

    def comer(self,numA:int):
        print(self.__nombre, "esta consumiendo: ",self.alacena[numA].printNombre())
        self.__energia = self.__energia + 0.8

    def dormir(self):
        print("Es hora de dormir, ha sido un dia muy largo...")
        print("")
        #Solicitaremos las horas para dormir
        while True:
            try:
                horas = float(input("¿Cuantas horas dormiremos? (Maximo podemos dormir 10 hrs): "))
                if ((horas<0) | (horas>10)):
                    raise RangoError("RangoError")
                else:
                    break

            except RangoError:
                print(self.__nombre," recuerda que solo podemos dormir de 1 a 10 horas")

            except ValueError:
                print(self.__nombre," el valor que ingresaste no es totalmente numerico")

        self.__energia = self.__energia + (horas * 1)

    def obtenerEstado(self):
        print("")
        print("Actualmente",self.__nombre, "se encuentra con:")
        print("Energia:             ",self.__energia)
        print("Saldo en cuenta ($): ", self.__credito)
        print("")

    def comprar(self):
        self.__energia = self.__energia - 0.15

    #Metodos GETTER y SETTER
    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def getEdad(self):
        return self.__edad

    def getEstudios(self):
        return self.__estudios

    def getCarrera(self):
        return self.__carrera

    def getTelefono(self):
        return self.__telefono

    def getEnergia(self):
        return self.__energia

    def getCredito(self):
        return self.__credito

    def setEnergia(self,newEnergia):
        self.__energia = newEnergia

    def setCredito(self,newCredito):
        self.__credito = newCredito


class Empleado(Persona):
    def __init__(self,empresa,salario,puesto,jornada,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,telefono,carrera=None,energia=10):
        self.__empresa = empresa
        self.__salario = salario
        self.__puesto = puesto
        self.__jornada = jornada
        super().__init__(nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,estudios,telefono,carrera,energia)
        self.__energia = super().getEnergia()

    def trabajar(self):
        print(super().getNombre()," ha iniciado su jornada laboral de: ",self.__jornada," horas en", self.__empresa)
        self.__energia = self.__energia - (self.__jornada * 0.5)
        super().setEnergia(self.__energia)
        print("")

    def recibirSalario(self):
        print("Ha llegado el dia de pago correspondiente a su semana laboral")
        pago = super().getCredito() + self.__salario
        super().setCredito(pago)
        print(super().getNombre(),"usted ha recibido: $",self.__salario)
        print("Gracias por su trabajo, nos vemos la semana entrante")

    #Metodos GETTER Y SETTER
    def getPuesto(self):
        return self.__puesto



#CLASES DE INTERACCION -------------------------------------
class Producto:
    def __init__(self,nombre,precio,categoria,descripcion):
        self.__nombre = nombre
        self.__precio = int(precio)
        self.__categoria = categoria
        self.__descripcion = descripcion

    def printNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def getCategoria(self):
        return self.__categoria

    def getDescripcion(self):
        return self.__descripcion


#CLASES DE ESTABLECIMIENTOS PARA INTERACTUAR -------------------------------------
class EstablecimientoDeServicios:
    def __init__(self,nombre,direccion,dueño,giro):
        self.__nombreEst = nombre
        self.__direccion = direccion
        self.__dueño = dueño
        self.__giro = giro

    def getNombreEst(self):
        return self.__nombreEst

    def getDireccion(self):
        return self.__direccion

    def getDueño(self):
        return self.__dueño

    def getGiro(self):
        return self.__giro

class Supermercado(EstablecimientoDeServicios):
    def __init__(self,nombre,direccion,dueño,giro,productos,ingresos):
        super().__init__(nombre,direccion,dueño,giro)
        self.productos = productos
        self.ingresos = ingresos

    def atenderVenta(self):
        i=1
        #Presentamos articulos a vender
        print("¿Que producto llevaras?")
        for articulos in (self.productos):
            print("{}.- {}. --> Precio: {}".format(i,articulos.printNombre(),articulos.getPrecio()))
            i=i+1
        print("")

    def vender(self,Comprador,productoComp):
        #Compra realizada con cargo a la persona instanciada
        cargo = (self.productos[productoComp-1].getPrecio())
        credito = Comprador.getCredito()
        Comprador.setCredito(credito-cargo)
        self.ingresos = self.ingresos + cargo

        #Agregamos articulo instanciado al comprador
        if (self.productos[productoComp-1].getCategoria() == "COMIDA"):
            Comprador.addAlacena(self.productos[productoComp-1])

        else:
            Comprador.addGuardaropa(self.productos[productoComp - 1])

        #Confirmamos compra
        print(Comprador.getNombre(),"ha comprado: ",self.productos[productoComp-1].printNombre())
        Comprador.comprar()     #Reflejamos fatiga tras ir de compras


class CYC(EstablecimientoDeServicios):
    def __init__(self,nombre,direccion,dueño,giro,gerente,finanzas,produccion,marketing,diseño=None):
        super().__init__(nombre,direccion,dueño,giro)
        self.__gerente = gerente
        self.__finanzas = finanzas
        self.__produccion = produccion
        self.__marketing = marketing
        self.entrevistados = []
        self.empleados = []
        self.ObjEntrevitados = []

    def addEmpleado(self,gerente,empleado):
        if (gerente.getPuesto() == "Gerente"):
            baseTemporal=[empleado.getNombre(),empleado.getApellidos(),empleado.getEdad(),empleado.getTelefono(),empleado.getEstudios(),empleado.getCarrera()]
            self.empleados.append(baseTemporal)

        else:
            print(gerente.getNombre(),"no corresponde al area de Gerencia, por lo tanto no puede recibir agregar los empleados vigentes")

    def verEmpleadosContratados(self):
        i = 0
        for empleados in self.empleados:
            print("EMPLEADO NUMERO: ", i, "------------------")
            print("Nombre: ", empleados[0])
            print("Apellidos: ", empleados[1])
            print("Edad: ", empleados[2])
            print("Telefono: ", empleados[3])
            print("Nivel de estudios: ", empleados[4])
            print("Carrera: ", empleados[5])
            print(" ")
            i = i + 1

    def gestionarFinanzas(self,trabajador):
        if (trabajador.getPuesto() == "Director Finanzas"):
            print(trabajador.getNombre(),"ha comenzado la gestion de Finanzas...")

        else:
            print(trabajador.getNombre(),"no corresponde al area de Finanzas, por lo tanto no puede Gestionar las Finanzas")

    def iniciarProduccion(self, trabajador):
        if (trabajador.getPuesto() == "Supervisor de Produccion"):
            print(trabajador.getNombre(), "ha iniciado la produccion del dia...")

        else:
            print(trabajador.getNombre(),"no corresponde al area de Produccion, por lo tanto no puede iniciar las ordenes del dia")

    def gestionarRedesSociales(self, trabajador):
        if (trabajador.getPuesto() == "Marketing"):
            print(trabajador.getNombre(), "ha comenzado la administracion de publicaciones en redes...")

        else:
            print(trabajador.getNombre(),"no corresponde al area de Marketing, por lo tanto no puede publicar en las redes de la empresa")

    def iniciarVisorias(self, trabajador):
        if (trabajador.getPuesto() == "Gerente"):
            print(trabajador.getNombre(), "ha comenzado las visorias para contratar")
            print("")

        else:
            print(trabajador.getNombre(),"no corresponde al area de Gerencia, por lo tanto no puede recibir los candidatos a contratar")

    def entrevistar(self, gerente,solicitante):
        baseTemporal=[]
        if (gerente.getPuesto() == "Gerente"):
            print(gerente.getNombre(),"esta entrevistando a ",solicitante.getNombre())
            print("+Gerente: Hola, bienvenido a C&C,mi nombre es: ",gerente.getNombre(),"soy el gerente y comenzaremos el proceso de entrevista. ¿Cual es tu nombre?")
            print("-Solicitante: Mi nombre es: ",solicitante.getNombre())
            print("+Gerente: ¿Cuales son tus apellidos?")
            print("-Solicitante: Mis apellidos son: ", solicitante.getApellidos())
            print("+Gerente: ¿Cuantos años tienes?")
            print("-Solicitante: Cuento con: ", solicitante.getEdad(),"años señor")
            print("+Gerente: ¿Cual es tu numero telefonico?")
            print("-Solicitante: Mi numero es: ", solicitante.getTelefono())
            print("+Gerente: ¿Cual es tu nivel maximo de estudios?")
            print("-Solicitante: Estudie la: ", solicitante.getEstudios(), "señor")
            print("+Gerente: ¿Cual es tu area de estudios o carrera?")
            print("-Solicitante: Mi carrra es: ", solicitante.getCarrera())
            print("+Gerente: De acuerdo ",solicitante.getNombre(),"tenemos la informacion necesaria, tenemos tu numero telefonico, nostros te llamamos")
            print(" ")

            #Almacenamos la informacion de cada entrevista para su posterior analisis
            baseTemporal=[solicitante.getNombre(),solicitante.getApellidos(),solicitante.getEdad(),solicitante.getTelefono(),solicitante.getEstudios(),solicitante.getCarrera()]
            self.entrevistados.append(baseTemporal)
            self.ObjEntrevitados.append(solicitante)

        else:
            print(gerente.getNombre(),"no corresponde al area de Gerencia, por lo tanto no puede recibir los candidatos a contratar")

    def analizarSolicitantes(self,gerente):
        if (gerente.getPuesto() == "Gerente"):
            i=0
            for solicitantes in self.entrevistados:
               print("SOLICITANTE NUMERO: ",i,"------------------")
               print("Nombre: ",solicitantes[0])
               print("Apellidos: ", solicitantes[1])
               print("Edad: ", solicitantes[2])
               print("Telefono: ", solicitantes[3])
               print("Nivel de estudios: ", solicitantes[4])
               print("Carrera: ", solicitantes[5])
               print(" ")
               i=i+1

        else:
            print(gerente.getNombre(),"no corresponde al area de Gerencia, por lo tanto no puede ver los candidatos a contratar")

    def contratar(self,gerente):
        if (gerente.getPuesto() == "Gerente"):
            # Solicitaremos la persona a contratar
            while True:
                try:
                    contratado = int(input("¿Ingrese el numero de entrevista correspondiente al postulado seleccionado?: "))
                    if ((contratado < 0) | (contratado > 3)):
                        raise RangoError("RangoError")
                    else:
                        break

                except RangoError:
                    print(self.__nombre, " ingrese un numero de entrevista existente")

                except ValueError:
                    print(self.__nombre, " el valor que ingresaste no es totalmente numerico")

            print("*Nuestro nuevo elemento en el area de diseño es ",self.entrevistados[contratado][0])
            print("*Llamando a: ",self.entrevistados[contratado][3],"...")
            print("Hola ",self.entrevistados[contratado][0],"habla",gerente.getNombre(),"gerente en C&C para notificar que ha sido contratado, muchas felicidades y bienvenido al equipo de trabajo")
            self.addEmpleado(gerente,self.ObjEntrevitados[contratado])

        else:
            print(gerente.getNombre(),"no corresponde al area de Gerencia, por lo tanto no puede contratar")




















