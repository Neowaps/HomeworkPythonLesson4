# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Введите длину первого набора множеств: "))
m = int(input("Введите длину второго набора множеств: "))
firstSet = list(randint(1,10) for i in range(n))
secondSet = list(randint(1,10) for i in range(m))
print(firstSet, secondSet)
result = []
for i in firstSet:
    if i in secondSet and i not in result:
        result.append(i)
result.sort()

print(result)
