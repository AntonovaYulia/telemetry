time_in_sec = int(input('Введите время в секуднах: '))
hour = time_in_sec // 3600
time = time_in_sec % 3600
minutes = time // 60
sec = time % 60

print(f'Ваше время в секундах {hour:02d}:{minutes:02d}:{sec:02d}')