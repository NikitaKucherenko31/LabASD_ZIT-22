import random
'''Дан одномерный массив из 15 элементов. Элементам массива меньше 10 присвоить
нулевые значения, а элементам больше 20 присвоить 1. Вывести на экран монитора
первоначальный и преобразованный массивы в строчку.'''
def binary_digits_array():
    Original_array = []
    Converted_array = []
    for i in range(15):
        Original_array.append(random.randrange(-5, 35))
        Converted_array.append(Original_array[i])
        if Original_array[i] < 10:
            Converted_array[i] = 0
        if Original_array[i] > 20:
            Converted_array[i] = 1
    print("Исходный массив: ", Original_array, "; Преобразованный массив:", Converted_array)
binary_digits_array()
