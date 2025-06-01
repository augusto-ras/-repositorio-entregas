entrada=[10,20,30,40]
valor=24
def si_promedio_lista_mayor_que_valor(lista:list,val:int)-> bool:
    promedio=0
    suma= 0
    for i in range(len(lista)):
       suma += lista[i]
    print(suma)
    promedio= suma/4
    print(promedio)
    if promedio > valor:
        respuesta=True 
    else:
        respuesta=False
    
    return respuesta
print(si_promedio_lista_mayor_que_valor(entrada,valor))


