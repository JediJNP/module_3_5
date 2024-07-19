print('Рекурсивное умножение цифр')
print('--------------------------')


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        result = first * get_multiplied_digits(int(str_number[1:]))
    else:
        result = first
    return (result)

number = (int(input('Введите двухзначное число: ')))
result = get_multiplied_digits(number)
print(result)

