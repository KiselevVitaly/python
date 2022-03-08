def num_translate_adv():
    number = input('Число на англ: ')
    if number.istitle():
        print(numbers.get(number.lower()).title())
    else:
        print(numbers.get(number))


numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num_translate_adv()
