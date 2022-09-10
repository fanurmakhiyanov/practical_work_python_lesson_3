# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# decimal_number = int(input("Введите число в десятичной СС: "))
# print(bin(decimal_number))

number = int(input("Введите число в десятичной СС: "))
numberb = ""

while number > 0:
    numberb = str(number % 2) + numberb
    number = number // 2
 
print(numberb)