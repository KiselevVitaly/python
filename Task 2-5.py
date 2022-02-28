price = [45.99, 33.33, 25.16, 64.75, 23.56, 0.55, 23.56, 74.44, 78.34, 86.23, 7, 23.75, 21.68, 11.79, 26.03]

for i in price:
    print(f'{int(i)} руб. {int(i * 100 % 100):02} коп.', end=', ')

print(f'\nid {price} id = {id(price)}')
price.sort()
print(f'id {price} id = {id(price)}')

price_sort = sorted(price, reverse=True)
print(f'{price_sort} id = {id(price_sort)}')

print(price[-5:])
