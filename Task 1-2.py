
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Решить задачу под пунктом b, не создавая новый список.

numbers = []
numbers_sum = 0
numbers_sum_17 = 0

for number in range(1, 1001, 2):
    number_cube = (number ** 3)
    numbers.append(number_cube)
    number_cube_17 = number_cube + 17
    number_sum = (sum(map(int, str(number_cube))))
    number_sum_17 = (sum(map(int, str(number_cube_17))))
    if number_sum % 7 == 0:
        numbers_sum = numbers_sum + number_cube
    elif number_sum_17 % 7 == 0:
        numbers_sum_17 = numbers_sum_17 + number_cube_17

print("Список =", numbers)
print("Сумма чисел списка, которые нацело делятся на 7 =", numbers_sum)
print("Сумма чисел списка (+17), которые нацело делятся на 7 =", numbers_sum_17)
