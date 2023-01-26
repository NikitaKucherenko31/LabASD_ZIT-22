import math
def reverse(number):
    if number<0:
        return -1
    elif number==0:
        return 0
    else:
        copy_number = number
        num_of_digit = 0  
        while copy_number>0:
            num_of_digit = num_of_digit+1
            copy_number = copy_number//10
        last_digit = number%10
        summ = last_digit * int(math.pow(10, num_of_digit-1))
        return summ + reverse(number//10)
number = int(input("Введите число: "))
print("Число в обратном порядке = ", reverse(number))
