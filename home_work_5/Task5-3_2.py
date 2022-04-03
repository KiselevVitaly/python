klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9A'
]

tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей', 'Мария',
'Дмитрий', 'Борис', 'Елена', 'Александр', 'Николай'
]

while len(klasses)<=len(tutors):
    klasses.append('None')


res_gen = ((tutors[i], klasses[i]) for i in range(0, len(tutors)))
print(*res_gen)