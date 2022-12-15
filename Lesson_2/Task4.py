# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число..


from random import randint

def list(N):
    list = []
    for i in range(N):
        list.append(randint(-N, N))
    return list

N = int(input('Введите число N: '))
num = list(N)
print(num)
a = open('file.txt','r')
res = num[int(a.readline())] * num[int(a.readline(2))]
print(res)