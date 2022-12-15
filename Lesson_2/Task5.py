#Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)

the_set = set()

for i in range(100000):
    the_set.add(str(i))

for e in the_set:
    print(int(e))
    break