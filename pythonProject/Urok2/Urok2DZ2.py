# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

number = int(input('Введите число: '))
multip = int(input('Теперь ведите произведение чисел: '))
diskr = number**2 - 4*(-1)*(-1)*multip
if diskr == 0:
    print(f'Два одинаковых числа: {(-1)*number/(2*(-1))}')
elif diskr > 0:
    print(f'Загаданы два одинаковых числа {((-1)*number + diskr**0.5)/(2*(-1))} и {((-1)*number - diskr**0.5)/(2*(-1))}')
else: print ('не правельно')