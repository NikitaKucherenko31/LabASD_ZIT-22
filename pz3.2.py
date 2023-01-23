from random import randint
'''Расположить столбцы матрицы D[M,N] в порядке
возрастания элементов k-й строки (1<=k<=M). '''
def sort_d():
    print("Введите размерность матрицы D[M,N]")
    m=int(input("Введите M:"))
    n=int(input("Введите N:"))
    k=int(input("Введите K (1<=k<=M):"))
    d = [[randint(1, 10) for j in range(n)] for i in range(m)]
    print(d)
    f = [(i, val) for i, val in enumerate(d[k-1].copy())] 
    f.sort(key=lambda e: e[1]) #сортировка по значению списка
    print(f)
    h = len(d[0]) 
    g = len(d) 
    new_d = []
    for i in range(g):
        new_d.append([])
        for j in range(h):
            new_d[i].append(d[i][f[j][0]])
    return new_d
print(sort_d())
