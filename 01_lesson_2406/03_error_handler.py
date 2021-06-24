while True:
    b = input('Number: ')
    c = input('Number 2: ')

    try:
        b = int(b)
        c = int(c)
        print(b / c)
        print('успех!')
    except ZeroDivisionError:
        print('Делить на ноль нельзя (неправда)')
