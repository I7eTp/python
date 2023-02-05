# Урок2 Дз №3.Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

sum_max = int(input('Введите положительное целое число ограничитель: '))
flag, i = True, 0
list_sum = []
while flag:
    if sum_max >= 2**i:
        list_sum.append(2**i)
        i += 1
    else:
        flag = False
print(f'2**k ограниченные числом {sum_max}: {list_sum}')

