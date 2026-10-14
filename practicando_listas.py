lista=[99,'hola',22.4,'nintendo']
#para agregar elementos a la lista: .append()
#para agregar elementos en la lista en una posicion especifica: .insert(posicion,'nuevo elemento')
#para invertir elementos de la lista: .reverse()
#ordenar de mayor a menor .sort(reverse=True)
#ordenar de menor a mayor .sort()
#unir listas: .extend()
#EJERCICIO 16: Registro dinámico de nombres
'''
nombres=[]
while True:
    inserta_nombre=input('inserta tu primer nombre: ')
    if inserta_nombre=='fin':
        break
    
    elif inserta_nombre in nombres:
        print('ese nombre ya existe,ingresa otro nombre')
        continue
        
    else:
        nombres.append(inserta_nombre)
print(nombres)
'''
#EJERCICIO 17:insertar elementos en posiciones especificas
'''
colores=['rojo','verde','azul']
print('indica si quieres colocar el color al inicio o al final\n')

while True:
    inserta_color=input('inserta un color (o escribe final para terminar): ')
    
    if inserta_color=='final':
        break
    elige_posicion=input('Elige posición primero/ultimo: ')
    
    if inserta_color in colores:
        print('ese color ya existe,ingresa otro color')
        
        continue
    if elige_posicion=='primero':
        colores.insert(0,inserta_color)
    elif elige_posicion=='ultimo':
        colores.append(inserta_color)
    else:
        print('posición inválida')
        continue
    
print(colores)
'''
#EJERCICIO 18: Ekiminar elementos por nombre
'''
frutas=['manzana','pera','uva','mango','pera']
while True:
    eliminar_fruta=input('ingresa la fruta que quieres eliminar(escribir stop para parar): ')

    if eliminar_fruta=='stop':
        break
    elif eliminar_fruta in frutas:
        frutas.remove(eliminar_fruta)
        print(f'se eliminó una {eliminar_fruta}')
    else:
        continue
print(frutas)
'''
#EJERCICIO 19:Eliminar por posición
'''
números=[1,2,3,4,5,6,7,8,9,10]
while True:
    eliminar_número=int(input('ingresa la ´psición del número a eliminar(escribir "-1" para deterner): '))
    if eliminar_número==-1:
        break
    elif eliminar_número>len(números):
        continue
    elif eliminar_número in números:
        del números[eliminar_número]

print(números)
'''
#EJERCICIO 20:Construir una lista filtrando datos
'''
lista_via=[]
while True:
    valor=input('ingresa el valor a ingresar: ')
    if valor=='terminar':
        break
    elif any(caracter.isdigit() for caracter in valor):
        continue
    elif len(valor)>10:
        continue
    lista_vacia.append(valor)
'''
#EJERCICIO 21:Lista de compras dinámica
'''
compras=[]
while True:
    producto=input('ingresa el producto que vas a comprar: ').strip().lower()
    if producto=='fin':
        break
    elif producto == '':
        print('No puedes ingresar un producto vacío.')
        continue
    elif producto in compras:
        print('ese producto ya existe,ingresa otro producto')
    elif any(caracter.isdigit() for caracter in producto):
        print('El producto no puede contener números.')
        continue
    else:
        compras.append(producto)
print(compras)
'''
#EJERCICIO 22:Insetar tareas con prioridad
'''
tareas=["cenar","estudiar","dormir"]
print('indica la prioridad de la tarea con las opciones (alta/baja)')
print('escribe salir para finalizar programa\n')
while True:
    nueva_tarea= input('Ingresa una nueva tarea:').strip().lower()
    elige_posicion=input('Elige posición alta/baja: ').strip().lower()
    
    if nueva_tarea=='salir':
        break
    
    elif nueva_tarea == '':
        print('No puedes ingresar una tarea vacía.')
        continue
    elif nueva_tarea in tareas:
        print('esa tarea ya existe,ingresa otra tarea')
        continue
    
    elif elige_posicion=='alta':
        tareas.insert(0,nueva_tarea)
    elif elige_posicion=='baja':
        tareas.append(nueva_tarea)
    else:
        print('posición inválida')
        continue
    
print(f'tu lista de tareas es {tareas}')
'''
#EJERCICIO 23:Eliminar pañabras prohibidas
texto=["sol","mar","arena","fuego","mar","aire"]
print('escribe "stop" para detener el programa\n')
while True:
    palabra_eliminada=input('ingresa palabra a eliminar: ').strip().lower()
