tablero=[[0,0,1,0,0],
         [0,1,0,1,0],
         [1,0,0,1,0],
         [0,0,1,0,1],
         [0,0,0,0,1]]


def batalla_naval(lista:list,x:int,y:int)->bool:
   
   for i in range(len(lista)):
      for j in range(len(lista[i])):
          if lista[x][y]== 1:
             respuesta=True
          else:
             respuesta=False
   return respuesta
hundidos=0
estado_de_juego="S"
while estado_de_juego=="S" or estado_de_juego=="s":
   
   corX=int(input("insertarar cordenada x(fila)"))
   corY=int(input("insertarar cordenada Y(fila)"))
   while corX<0 or corX>4 or corY<0 or corY>4:
      print ("no es valido")
      corX=int(input("insertarar cordenada x(fila)"))
      corY=int(input("insertarar cordenada x(fila)"))
   if batalla_naval(tablero,corX,corY)==True:
      print("Hundido")
      hundidos= hundidos + 1
   else:
      print("Agua")
   estado_de_juego=(input("segir jugando S/N: "))
   if estado_de_juego=="N" or estado_de_juego=="n":
      print("hundiste",hundidos,"barcos")
   while estado_de_juego!="S" and estado_de_juego!="s" and estado_de_juego!="N" and estado_de_juego!="n":
      estado_de_juego=(input("segir jugando S/N: "))
      if estado_de_juego=="N" or estado_de_juego=="n":
         print("hundiste",hundidos,"barcos")