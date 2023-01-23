'''Вводим последовательность натуральных чисел, завершающуюся 0. Определите
наибольшее значение числа в этой последовательности.'''
arr=[]
def max_elem_arr(arr):
    n=int(input("Введите элемент массива: "))
    if n==0:
        return max(arr)
    else:
        arr.append(n)
        return max_elem_arr(arr)
print(max_elem_arr(arr))
