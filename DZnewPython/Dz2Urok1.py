# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

zurav = input('Видите сумму всех изготовлиных журавликов: ')
zurav = int(zurav)
print('Всего изготовлено журавликов', zurav)
pro=(zurav//3)
Kat=(pro*2)
PetSer=(zurav-Kat)
print('Катя сделала:', Kat)
print('Петя и Сережа сделали:', PetSer)