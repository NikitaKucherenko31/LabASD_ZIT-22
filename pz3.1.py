from random import randint
'''Найти максимальный среди всех элементов тех строк заданной матрицы,
которые упорядочены (либо по возрастанию, либо по убыванию).'''
def maximal_element():
    arr = [[randint(1, 10) for j in range(3)] for i in range(3)]
    print(arr)
    print(max([max(row) for row in arr if row == sorted(row) or row == sorted(row, reverse=True)]))
maximal_element()
