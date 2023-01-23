from random import randint
'''Определите, есть ли в списке повторяющиеся элементы, если да,
то вывести на экран это значение, иначе сообщение об их отсутствии.'''
def duplicate_elements():
    Arr = [randint(-10,30) for i in range(8)]
    print(Arr)
    duplicates = [i for i in set(Arr) if Arr.count(i) > 1]
    if len(duplicates) != 0:
        print(duplicates)
    else:
        print("Повторяющихся элементов нет!")
duplicate_elements()
