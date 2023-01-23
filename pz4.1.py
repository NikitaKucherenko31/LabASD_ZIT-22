'''Найти максимальный среди всех элементов тех строк заданной матрицы,
которые упорядочены (либо по возрастанию, либо по убыванию).'''
def maximal_element():
    f = open("pz4.1_KucherenkoNA_input.txt", "r")
    arr = [list(map(int, i.split())) for i in f.readlines()]
    print(arr)
    max_el=max([max(row) for row in arr if row == sorted(row) or row == sorted(row, reverse=True)])
    f2 = open("pz4.1_KucherenkoNA_output.txt", "w")
    f2.write(str(max_el))
    return max_el
print(maximal_element())


