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



#Instanciamos EMPLEADO - PERSONA de enfoque o interes
Franco = E4.Empleado("C&C",8000,"Gerente",8,"Franco","Calzadas",25,1.80,77,10000,"07-03-2030","Licenciatura","Ing Mecatronica",10)

Franco.obtenerEstado()          #Observamos el estado de cuenta y energia inicial
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

Franco.obtenerEstado()          #Observamos el estado de cuenta tras compras realizadas

Franco.mostrarGuardaropa()
Franco.vestir(0)
Franco.vestir(1)
Franco.vestir(2)
Franco.vestir(3)
Franco.vestir(4)
Franco.vestir(5)
Franco.vestir(6)