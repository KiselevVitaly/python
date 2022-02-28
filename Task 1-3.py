# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
#  Эм ну ок. Типа лол
for count in range(1, 101):
    number = str(count)
    exception = [12, 13, 14]
    if number[-1] == "1" and count != 11:
        print(number, "процент")
    elif int(number[-1]) >= 2 and int(number[-1]) <= 4 and count != exception:
        print(number, "процента")
    else:
        print(number, "процентов")