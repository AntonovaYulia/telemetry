proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
workers = int(input('Введите количество сотрудников: '))
profit = proceeds - costs
rent = profit / proceeds
salary = profit / workers
while True:
    if proceeds > costs:
        print(f'Вы молодцы, продолжайте в том же духе, прибыль: {profit:.2f}')
        print(f'Соотношение прибыли к выручке: {rent:.2f}')
        print(f'Прибыль фирмы в расчете на одного сотрудника: {salary:.2f}')
        break
    elif proceeds < costs:
        print(f'Выручка меньше издержок : {profit:.2f},  нужно поднажать!')
        break
    else:
        print(f'Выручка и издержки одинаковы, прибыль равна {profit:.2f}, удачи!')
        break