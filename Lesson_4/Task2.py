# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
n = 2
arr = []
ez = num
while n <= num:
    if num % n == 0:
        arr.append(n)
        num //= n
        n = 2
    else:
        n += 1
print(f"Простые множители числа {ez} приведены в списке: {arr}")