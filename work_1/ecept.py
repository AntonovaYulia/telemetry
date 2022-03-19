def devizion(number_1, number_2):
    result = 0
    try:
        result = number_1/ number_2
    except ZeroDivisionError as error:
        result = 'Попытка деления на ноль'
        for s in error.__class__.__mro__:
            print(s.__name__)

            return result



        print(devizion(2,4))
        print(devizion(4, 2))

        print(devizion(2,0))