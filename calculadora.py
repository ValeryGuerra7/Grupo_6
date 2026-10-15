
n = int(input("tamaño de la suma: "))
suma = 0 
for i in range(n):
    s = int(input("número: "))
    suma = suma + s
print("suma es",suma)
    

'''
def multiplicacion():
    m = int(input("tamaño de la multiplicación; "))
    multi = 1
    for i in range(m):
        l = int(input("número: "))
        multi = multi * l
    print("producto es",multi)
    return multi

# suma del triangulo superior

def sum_matriz_trian_sup(A):
    s = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i <= j:
                s = s + A[i][j]
    print(s)
    return s

D = [[1,2,3],[4,5,6],[7,8,2]]
X = sum_matriz_trian_sup(D)

def resta():
    a = float(input("Primer número (minuendo): "))
    b = float(input("Segundo número (sustraendo): "))
    resultado = a - b
    print("La diferencia es", resultado)
    return resultado

def division():
    a = float(input("Numerador: "))
    b = float(input("Denominador: "))
    if b == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    resultado = a / b
    print("El cociente es", resultado)
    return resultado
'''
'''
def sumar(a, b):
    return a + b

print("Calculadora del grupo 6 - Modificado por Sergio Mendoza Chavez")
print("Suma 5 + 3 =", sumar(5, 3))
'''


