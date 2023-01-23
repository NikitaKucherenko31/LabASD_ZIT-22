'''Вывести число в обратном порядке.'''
def reverse(number): 
    global reverse_number
    if (number > 0): 
        digit = number % 10 
        reverse_number = (reverse_number * 10) + digit 
        reverse(number // 10) 
    return reverse_number
number = int(input("Введите число: ")) 
reverse_number = 0
reverse_number = reverse(number) 
print("Число в обратном порядке = ", reverse_number)
