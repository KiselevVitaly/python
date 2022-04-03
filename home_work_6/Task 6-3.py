from itertools import zip_longest
import json


with open('Data/users.csv', 'r', encoding='utf-8') as name,\
        open('Data/hobby.csv', 'r', encoding='utf-8') as hobby:
            names = name.read().splitlines()
            hobbys = hobby.read().splitlines()

if len(names) < len(hobbys):
    print(1)
else:
    user_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    print(user_hobby)
    with open('Data/users_hobby_dict.txt', 'w', encoding='utf-8') as f:
        json.dump(user_hobby, f, ensure_ascii=False)