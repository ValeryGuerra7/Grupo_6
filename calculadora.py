
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
'''
