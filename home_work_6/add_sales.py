import sys


with open('Data/bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[1]}\n')
exit()