start = float(input('Введите число км : '))
finish = float(input('Введите конечную цель: '))
day = 1

if start > finish:
    print(day)
while True:
    if start <= 0 or finish <= 0:
        print('Результат должен быть больше нуля! Стартовое значение != 0')
    else:
        while start < finish:
            start = start + start/10
            day += 1
        print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {finish} км.')
        break