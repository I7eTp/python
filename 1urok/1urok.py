number = float(input('введите значение a: '))
if number % 2 == 0:
    print('нет')
else:
    print(f'{(number*10)%10}')
