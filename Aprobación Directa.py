#Augusto Scarafia
#Título: Gestión de Ventas de Productos con Lista/Array y Matriz en Python
#Descripción: Se dispone de una lista/array de 3 productos: A, B y C, y una matriz que contiene las ventas
#trimestrales de cada producto (en miles de dólares).
#Cada fila de la matriz representa a un producto, y cada columna representa un trimestre (T1, T2, T3).
from funciones_Aprobación_Directa  import *
# datos iniciales 
productos=["A", "B" ,"C"]
VENTAS=[
    [50,60,70],
    [80,55,45],
    [40,65,75]
]
#Menu 
estado_menu=0
while estado_menu==0:
 print("----Menú de opciones----\n" \
 "1.Mostrar productos y ventas.\n" \
 "2 Ordenar los productos de mayor a menor según sus ventas totales anuales.\n" \
 "3.Buscar un producto por nombre y mostrar sus ventas.\n" \
 "4.Buscar un valor de venta dentro de la matriz y mostrar a qué producto y trimestre pertenece.\n" \
 "5.salir.")
 opcion=int(input("elegir una opcion del menu entre (1 - 5): "))
 while opcion>5 or opcion<1:
     print("opcion no valida " )
     opcion=int(input("elegir una opcion del menu entre (1 - 5): "))
    
 if opcion==1:
     Mostrar_productos_y_ventas(productos,VENTAS)

 elif opcion==2:
    #llamar funsion2
     Ord_productos_mayor_menor_total(productos,VENTAS)

 elif opcion==3:
     #llamar funsion3
     Buscar_un_producto_por_nombre(productos,VENTAS)

 elif opcion==4:
     #llamar funsion4
     Buscar_valor_venta_de_matriz_mostrar_producto_trimestre(productos,VENTAS)

 elif opcion==5:
     print("-------Elegiste 5.salir------- \n            Adios :)") 
     estado_menu=1