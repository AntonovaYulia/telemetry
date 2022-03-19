def devizion(a, b, c):

try:
    D = (b**2)-4*a*c
x1 = (-b + math.sqrt(D)) / 2 * a
x2 = (-b - math.sqrt(D)) / 2 * a
except TypeError:
D = f'{a},{b},{c} Переменная должна быть числом'
except UnboundLocalError:
x1 = 'Корня нет'
x2= 'Корня нет'
except ValueError:
x1 = 'Корня нет'
x2 = 'Корня нет'

return D, x1, x2


print(devizion(int(input("Введите a:")), int(input("Введите b: ")), int(input("Введите c:"))))


import matplotlib.pyplot as plt
import numpy as np
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третий число:'))
x = np.linspace(-100,100, 100)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="y(x)")
ax.set_xlabel("x") # подпись у горизонтальной оси х
ax.set_ylabel("y") # подпись у вертикальной оси y
ax.legend() # показывать условные обозначения

plt.show() # показать рисунок
fig.savefig('1.png') # сохранить в файл 1.png