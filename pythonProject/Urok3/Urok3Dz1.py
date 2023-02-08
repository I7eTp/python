# Урок 3. Дз1. Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
list_num = [random.randint(0, 100) for _ in range(0, int(input('Введите длину списка: ')))]
print(list_num)
num = int(input('Введите искомое число X: '))
min_left, min_right = min(list_num), max(list_num)
count = 0
for i in list_num:
    if i == num:
        count += 1
    elif num > i:
        if num-i < num - min_left:
            min_left = i
    elif num < i:
        if i - num < min_right - num:
            min_right = i
if count > 0:
    print(f'Число {num} встречается {count} {"раз" if count == 1 else "раза"}')
else:
    if num > min(list_num):
        print(f'Число {num} максимально близко ему слева {min_left}')
    if num < max(list_num):
        print(f'Число {num} максимально близко ему справа {min_right}')