#Enunciado/s:
#Tabla de Posiciones de Torneo de Ping-Pong
#Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
#Los datos que se cargarán son:
#Nombre del jugador
#Edad (validar)
#Cantidad de puntos (validar-número entero positivo, hasta 60).
#número de partidos ganados (validar-número entero positivo, hasta 35).
#Tipo de saque ("plano", "liftado", "cortado")
#Categoría ("elite", "experto", "avanzado")
#Se necesita saber
#Tema A:
#1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
#inclusive.
#2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
#3-Porcentaje de jugadores de categoría "experto".
#4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
#5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.

def jugadores_ping_pong()->list:
    estado_enduesta="S" 
    lista_de_encuesta=[]
    while estado_enduesta=="S" or estado_enduesta=="s":
      lisa_vasia=[]
      nom=input("Nombre del jugador: ")
      edad=int(input("edad del jugador: "))
      Puntasion=int(input("cantidad de puntos : "))
      victorias=int(input("cantidad de victorias : "))
      saque=input("saque(plano,liftado,cortado): ")
      categoria=input("Categiria(elite,experto,avanzado): ")
      while edad<0:
         print("edad no validad" )
         edad=input("edad del empleado: ")
      while Puntasion <0 or Puntasion >60 or Puntasion!= int:
         print("Puntasion no validad" )
         Puntasion=int(input("cantidad de puntos : "))
      while victorias <0 or victorias >35 or victorias!= int:
         print("victorias no validad" )
         victorias=int(input("cantidad de victorias : "))
      while saque!="plano" and saque!="liftado" and saque!="cortado":
         print("saque no validad" )
         saque=input("saque(plano,liftado,cortado): ")
      while categoria!="elite" and categoria!="experto" and categoria!="avanzado":
         print("categoria no validad" )
         categoria=input("Categiria(elite,experto,avanzado): ")
      lisa_vasia.append(nom,)
      lisa_vasia.append(edad)
      lisa_vasia.append(Puntasion)
      lisa_vasia.append(victorias)
      lisa_vasia.append(saque)
      lisa_vasia.append(categoria)
      print(lisa_vasia)
      lista_de_encuesta.append(lisa_vasia)
      estado_enduesta=(input("segir  S/N: "))
    
    return lista_de_encuesta

def chequeo_jugadores(lista1:list):
   caso1=0
   total=0
   sumacaso4=0
   for i in range(len(lista1)):
      total+=1
      for j in range(len(lista1[i])):
         if lista1[i][j]=="elite":
            if lista1[i][4]=="plano":
               if lista1[i][1] >19 or lista1[i][1] <25:
                  caso1+=1
         elif lista1[i][3] >50:
            if lista1[i][1] <17 :
               print(lista1[i][0])
               print(lista1[i][5])
         elif lista1[i][j]=="experto":
            exper+=1
            print("el personaje experto es",exper/total)
         elif lista1[i][j]=="avanzado":
            sumacaso4+=lista1[i][1]
            print ("el prodemdio es ",sumacaso4 /total)
        
