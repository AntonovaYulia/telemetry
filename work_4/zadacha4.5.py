def rewrite_file():
    try:
        with open('filsse.txt', 'r+') as file:
            file.write(input('Введите числа через пробел: '))
            l = map(int, file.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()