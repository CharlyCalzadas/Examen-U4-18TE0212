"""
MAIN. En este archivo se accedera a todas las clases desarrolladas y se trabajara con ellas
"""

import ExamenU4 as E4

#Creamos SUPERMERCADO con productos en existencia para su compra
productos = []

#Productos de tipo: ROPA
pantalonVestir = E4.Producto("Pantalon de Vestir",250,"ROPA","Color negro, corte recto")
productos.append(pantalonVestir)
zapatos = E4.Producto("Zapatos",600,"ROPA","Color negros, Estilo Italiano")
productos.append(zapatos)
calcetas = E4.Producto("Calcetas",15,"ROPA","Color Gris Oscuro, Dibujo Rombos")
productos.append(calcetas)
cinturon = E4.Producto("Cinturon",150,"ROPA","Color Negro, Relieve marcado")
productos.append(cinturon)
camisa = E4.Producto("Camisa",250,"ROPA","Color Azul Marino")
productos.append(camisa)
corbata = E4.Producto("Corbata",100,"ROPA","Color Negro")
productos.append(corbata)
saco = E4.Producto("Saco",450,"ROPA","Color Negro con 3 BOTONES")
productos.append(saco)

#Productos de tipo: COMIDA
huevo = E4.Producto("Huevo",3,"COMIDA","Huevo San Rafael")
productos.append(huevo)
tostada = E4.Producto("Tostada Integral",4,"COMIDA","Tostada Integral adquirido por pieza")
productos.append(tostada)
jitomate = E4.Producto("Jitomate",2,"COMIDA","Jitomate adquirido por pieza")
productos.append(jitomate)
chile = E4.Producto("Chile Verde",2,"COMIDA","Chile Verde adquirido por pieza")
productos.append(chile)

#Instanciamos SUPERMERCADO con productos existentes
Chedraui = E4.Supermercado("Chedraui","Zona Centro","Don Chedraui","VENTAS",productos,0)


#Instanciamos EMPLEADOS SECUNDARIOS DE EMPRESA
Pablo = E4.Empleado("C&C",7500,"Supervisor de Produccion",8,"Pablo","Santiago",30,1.70,115,150000,"08-05-2000","Licenciatura",2311587589,"Ing Mecatronica",9)
Eduardo = E4.Empleado("C&C",7500,"Director Finanzas",8,"Eduardo","Vazquez",30,1.68,70,85000,"05-11-2000","Licenciatura",2313694589,"Ing Mecatronica",9)
Luis = E4.Empleado("C&C",7500,"Marketing",8,"Luis","Pozos",32,1.78,90,95000,"01-02-1998","Licenciatura",2315894721,"Ing Mecatronica",9)

#Instanciamos PERSONAS (Sin empleo) para solicitar trabajo en C&C
Julie = E4.Persona("Julie","Cid",29,1.65,52,120000,"01-09-2001","Licenciatura",2352554578,"Diseño Industrial",11)
Grecia = E4.Persona("Grecia","Martinez",25,1.67,55,75000,"07-03-2030","Licenciatura",2382551446,"Ing Mecanico Electrica",11)
Matt = E4.Persona("Mattew","Murdock",36,1.77,80,150000,"05-10-2002","Licenciatura",2318974556,"Ing Industrial",11)

#Instanciamos EMPLEADO - PERSONA de enfoque o interes
Franco = E4.Empleado("C&C",8000,"Gerente",8,"Franco","Calzadas",25,1.80,77,10000,"07-03-2030","Licenciatura",2313195814,"Ing Mecatronica",10)
Franco.obtenerEstado()          #Observamos el estado de cuenta y energia inicial

#FRANCO PROCEDE A DORMIR (A partir de este punto inicia la interaccion en el dia a dia de Franco)
print("* Precenciaremos un dia en la vida de Franco, todo inicia en la noche de un dia Domingo")
print("* Franco se dispone a dormir")
Franco.dormir()
Franco.obtenerEstado()          #Observamos el estado de  energia tras dormir +AUMENTO

#FRANCO PROCEDE A IR A COMPRAR ROPA Y COMIDA ANTES DE IR A TRABAJAR
print("* Tras despertar, Franco decide ir a comprar ropa y comida")
Chedraui.atenderVenta()
Chedraui.vender(Franco,1)
Chedraui.vender(Franco,2)
Chedraui.vender(Franco,3)
Chedraui.vender(Franco,4)
Chedraui.vender(Franco,5)
Chedraui.vender(Franco,6)
Chedraui.vender(Franco,7)
Chedraui.vender(Franco,8)
Chedraui.vender(Franco,9)
Chedraui.vender(Franco,10)
Chedraui.vender(Franco,11)

Franco.obtenerEstado()          #Observamos el estado de cuenta tras y energia tras compras realizadas -DISMINUYO

#FRANCO PROCEDE A IR A COMPRAR ROPA Y COMIDA ANTES DE IR A TRABAJAR
print("* Franco regresa a casa y procede a vestirse")
Franco.mostrarGuardaropa()
Franco.vestir(0)
Franco.vestir(1)
Franco.vestir(2)
Franco.vestir(3)
Franco.vestir(4)
Franco.vestir(5)
Franco.vestir(6)

Franco.obtenerEstado()          #Observamos la energia tras vestirse -DISMINUYO

#FRANCO SE REALIZA UN OMMELETE ESTILO MEXICANO
print("* Tras estar vestido, nuestro protagonista decide desayunar antes de ir a trabajar")
Franco.mostrarAlacena()
Franco.comer(0)
Franco.comer(1)
Franco.comer(2)
Franco.comer(3)

Franco.obtenerEstado()          #Observamos la energia tras comer +AUMENTO

#FRANCO PROCEDE A IR A TRABAJAR
print("* Una vez descansado, vestido y desayunado, Franco procede a ir a trabajar")
Franco.trabajar()



#ANALIZAREMOS EL ENTORNO DE TRABAJO DE FRANCO YA QUE INICIO SU JORNADA LABORAL
CYC = E4.CYC("C&C","Zona Industrial","Charly Calzadas","Manufactura",Franco,Eduardo,Pablo,Luis)

print("* Inician las actividades del dia a dia en la empresa C&C correspondiente a su area")
CYC.gestionarFinanzas(Eduardo)
CYC.iniciarProduccion(Pablo)
CYC.gestionarRedesSociales(Luis)

print("")
print("* Imaginemos que Franco desea realizar actividades del area que no le corresponde:")
CYC.gestionarFinanzas(Franco)
CYC.iniciarProduccion(Franco)
CYC.gestionarRedesSociales(Franco)

print("")
print("* Sin embargo, Franco al ser de gerencia puede comenzar con las visorias de contratacion")
CYC.contratar(Franco)
CYC.entrevistar(Franco,Grecia)
CYC.entrevistar(Franco,Julie)
CYC.entrevistar(Franco,Matt)

print("* Una vez entrevistados, Franco procede a revisar las solicitudes")
CYC.analizarSolicitantes(Franco)



Franco.obtenerEstado()          #Observamos la energia tras una jornada de trabajo -DISMINUYO