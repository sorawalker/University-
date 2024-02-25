from math import *

def number_to_words(number: float) -> str:
    number = round(number, 3)
    units = number % 10
    tens = number - units
    if tens > 99 and tens not in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        tens -= 100 * int(str(tens)[0])
    elif tens in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        tens = 0
    hundreds = number - tens - units
    ost = 0
    try:
        ost = int(str(number).split('.')[1]) % 1000
    except IndexError:
        pass
    digit = int(number // 1)
    if ((number < 20) or (number in [20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900])) and ost == 0:
        return digits_to_words.get(number)
    elif ost != 0:
        return number_to_words(digit) + ' и ' + number_to_words(ost) + ' ' + digits_to_words.get(str(len(str(number).split('.')[1])))
    elif number > 100:
        if tens == 0:
            return digits_to_words.get(hundreds)+' ' + digits_to_words.get(units)
        elif hundreds == 0:
            return digits_to_words.get(tens) + ' ' + digits_to_words.get(units)
        elif units == 0:
            return digits_to_words.get(hundreds) + ' ' + digits_to_words.get(tens)
        elif tens == hundreds == 0:
            return digits_to_words.get(units)
        elif tens == units == 0:
            return digits_to_words.get(hundreds)
        elif units == hundreds == 0:
            return digits_to_words.get(tens)
        return digits_to_words.get(hundreds) + ' ' + digits_to_words.get(tens) + ' ' + digits_to_words.get(units)
    else:
        return digits_to_words.get(tens) + ' ' + digits_to_words.get(units)


def words_to_numbers(number: str) -> str:
    res = ''
    temp = ''
    for word in number.split():
        if words_to_digits.get(word) != None:
            if word in ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто', 'сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']:
                if temp != '':
                    temp = str(int(temp) + words_to_digits.get(word))
                else:
                    temp = str(words_to_digits.get(word))
                continue
            else:
                if temp != '':
                    res += str(int(temp) + words_to_digits.get(word))
                    temp = ''
                else:
                    res += str(words_to_digits.get(word))
    if temp != '':
        res += temp
    return res



def calc(s):
    n = words_to_numbers(s)
    print(eval(n))


digits_to_words = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот',
    'и': '.',
    'одна': 1,
    'две': 2,
    '1': 'десятых',
    '2': 'сотых',
    '3': 'тысячных',
    '4': 'десятитысячных',
    '5': 'стотысячных',
    '6': 'миллионных'
}

words_to_digits = {
    'трех':3,
    'четырех':4,
    'пяти':5,
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'плюс': '+',
    'минус': "-",
    'умножить': '*',
    'открывается': '(',
    'закрывается': ')',
    'разделить': '/',
    'остаток': '%',
    'и': '.',
    'одна': 1,
    'две': 2,
    'степени': '**',
    'пи': pi,
    'синус': 'sin(!)',
    'косинус': 'cos(!)',
    'тангенс': 'tg(!)',
    'котангенс': 'ctg(!)',
    'размещений': 'accommodation(!)',
    'сочетаний': 'combination(!)',
    'перестановок': 'permutation(!)',
}


def main():
    try:
        calc(input())
    except SyntaxError:
        print('Ошибка в вводе.')
        print('Введите заново:')
        main()
    except TypeError:
        print('Ошибка в вводе.')
        print('Введите заново:')
        main()
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


if __name__ == '__main__':
    main()