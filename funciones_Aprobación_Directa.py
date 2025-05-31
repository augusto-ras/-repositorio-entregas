def Mostrar_productos_y_ventas(lista1:list , lista2:list):
    #print listas 
 print("Elegiste 1.Mostrar productos y ventas.")
 for i in range(len(lista2)):
     print("Producto",lista1[i],end=" ventas " )
     for j in range(len(lista2[i])):
          print(lista2[i][j], end=" ") 
     print("")
 input("")
 


 

def Ord_productos_mayor_menor_total(lista1:list,lista2:list):
 print("Elegiste 2 Ordenar los productos de mayor a menor según sus ventas totales anuales.\n")
 suma = []
 for i in range(len(lista2)):
    #print(lista1[i],end=" " )
    suma_columna = 0
    for j in range(len(lista2)):
        suma_columna += lista2[i][j]
    suma.append(suma_columna)
    for i in range(0, len(suma)-1):
       for j in range(0, len(suma,)-i-1):
         if suma[j]  < suma[j+1] :
             suma[j], suma[j+1] = suma[j+1], suma[j]
             lista1[j],lista1[j+1]=lista1[j+1],lista1[j]
             lista2[j],lista2[j+1]=lista2[j+1],lista2[j]
 for i in range(len(suma)):
      print("Producto:",lista1[i],end=" |Ventas: ") 
      for j in range(len(lista2[i])):
           print(lista2[i][j], end=" |")
      print("Total:",suma[i],"|") 
      
 input("")

def Buscar_un_producto_por_nombre(lista1:list , lista2:list):
   print("Elegiste 3.Buscar un producto por nombre y mostrar sus ventas.")
   opcion=input("cual producto: ")
   numero_valido=0
   for i in range(len(lista1)):
      if lista1[i]== opcion:
         print("Producto",lista1[i], end="| ")
         for j in range(len(lista2[i])):
             print("T",j+1,":",lista2[i][j], end="| ")
             numero_valido=1
   while numero_valido==0:
      print("error no valido")
      opcion=input("cual producto: ")
      for i in range(len(lista1)):
        if lista1[i]== opcion:
         print(lista1[i], end="| ")
         for j in range(len(lista2[i])):
             print("T",j+1,":",lista2[i][j], end="|")
             numero_valido=1
   input("\n")    

def Buscar_valor_venta_de_matriz_mostrar_producto_trimestre(lista1:list , lista2:list):
   print("Elegiste 4.Buscar un valor de venta dentro de la matriz y mostrar a qué producto y trimestre pertenece.")
   numero_valido=0
   Valor=int(input("Cual valor quiere buscar :"))
   for i in range(len(lista2)):
       for j in range(len(lista2[i])):
          if Valor==(lista2[i][j]):
             print ("Producto",lista1[i]," trimestre ",j+1) 
             numero_valido=1
   while numero_valido==0:
      Valor=int(input("Cual valor quiere buscar :"))
      for i in range(len(lista2)):
          for j in range(len(lista2[i])):
             if Valor==(lista2[i][j]):
                print ("Producto",lista1[i]," trimestre ",j+1) 
                numero_valido=1
   input("") 
