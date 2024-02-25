import sys


def sum_of_n(numbers):
    sum_of_numbers = 0.0
    for numb in numbers:
        try:
            sum_of_numbers += float(numb)
        except:
            raise ValueError('Не все переданные значения числа')
    return sum_of_numbers


def mult_of_n(numbers):
    mult_of_numbers = 1
    for numb in numbers:
        try:
            mult_of_numbers *= float(numb)
        except:
            raise ValueError('Не все переданные значения числа')
    return mult_of_numbers

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Указано неверное количество аргументов')
    if sys.argv[1] == 'sum':
        print(sum_of_n(sys.argv[2:]))
    elif sys.argv[1] == 'mult':
        print(mult_of_n(sys.argv[2:]))
    else:
        print('Выбран неверный режим работы скрипта')