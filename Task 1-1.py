# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;python очистка терминала
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек

minutes = 60
hour = 60 * minutes
day = hour * 24

while not False:
    duration = int(input('Введите длительность (сек): '))
    calc_day = duration // day
    calc_hour = int((duration % day) / hour)
    calc_min = int((duration % hour) / minutes)
    seconds = duration % minutes
    if duration <= 0:
        print('Длительность не может быть отрицательная или равна 0!')
    elif duration < 60:
        print(duration, " сек")
    elif 60 <= duration < hour:
        print(calc_min, " мин", seconds, " сек")
    elif hour <= duration < day:
        print(calc_hour, "час", calc_min, "мин", seconds, "сек")
    else:
        print(calc_day, "дн", calc_hour, "час", calc_min, "мин", seconds, "сек")
