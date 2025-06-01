#Las posibles aplicaciones son las siguientes:
#● Inteligencia artificial (IA),
#● Realidad virtual/aumentada (RV/RA),
#● Internet de las cosas (IOT)
#Para ello, la empresa realiza entre sus empleados una encuesta, con el
#propósito de conocer ciertas métricas.
#A) Los datos a ingresar por cada empleado encuestado son:
#● nombre del empleado
#● edad (no menor a 18)
#● género (Masculino - Femenino - Otro)
#● tecnologia (IA, RV/RA, IOT)
#B) Cargar por terminal 10 encuestas.
#C) Determinar:
#1. Cantidad de empleados de género masculino que votaron por IOT o IA,
#cuya edad esté entre 25 y 50 años inclusive.
#2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
#género no sea Femenino o su edad se encuentre entre los 33 y 40.
#3. Nombre y tecnología que votó, de los empleados de género masculino con
#mayor edad de ese género.

def encuesta_datos()->list:
    estado_enduesta="S" 
    lista_de_encuesta=[]
    while estado_enduesta=="S" or estado_enduesta=="s":
      lisa_vasia=[]
      nom=input("Nombre del empleado: ")
      edad=int(input("edad del empleado: "))
      genero=input("genero del empleado(Masculino - Femenino - Otro): ")
      tecnologia=input("tecnolofia del empleado(IA, RV/RA, IOT): ")
      while edad<18:
         print("edad no validad" )
         edad=input("edad del empleado: ")
      while genero !="Masculino" and genero !="Femenino" and genero !="Otro":
         print("genero no validad" )
         genero=input("genero del empleado(Masculino - Femenino -Otro): ")
      while tecnologia!="IA" and tecnologia!="RV/RA" and tecnologia!="IOT":
         print("tecmologia no validad" )
         tecnologia=input("tecnolofia del empleado(IA, RV/RA, IOT): ")
      lisa_vasia.append(nom,)
      lisa_vasia.append(edad)
      lisa_vasia.append(genero)
      lisa_vasia.append(tecnologia)
      print(lisa_vasia)
      lista_de_encuesta.append(lisa_vasia)
      estado_enduesta=(input("segir  S/N: "))
    
    return lista_de_encuesta

encuestas=encuesta_datos()
#encuestas=[["A",40,"Masculino","IOT"],
          # ["mes",35,"Otro","IA"],
          # ["mes",20,"Femenino","IA"]]
print(encuestas)
#print(encuesta_datos)

def chequiarlista(lista:list):
   total=0
   contador2=0
   contador1=0
   for i in range(len(lista)):
      total+=1
      for j in range(len(lista[i])):
         if lista[i][j]=="Masculino":
            if lista[i][j-1] >25 or lista[i][j-1]<50:
               if lista[i][j+1] == "IOT" or lista[i][j+1] == "IA":
                  contador1+=1
            if lista[i][j+1] != "IA":
               if lista[i][1] >33 or lista[i][1]<40:
                  contador2+=1
            mayor=(lista[i][0] ,lista[i][3])
            if lista[i][j-1] < lista[i+1][j-1]:
                 mayor=(lista[i][0], lista[i][3])
         elif lista[i][j]=="Otro":
            if lista[i][j+1] != "IA":
               if lista[i][j-1] >33 or lista[i][j+1]<40:
                  contador2+=1
   print("1:",contador1)
   print("total:  ",total)
   print("contador2",contador2)
   print("2:",contador2 / total)
   print("3:",mayor)
   
chequiarlista(encuestas)