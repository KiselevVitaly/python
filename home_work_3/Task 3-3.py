def thesaurus(*args):
    dict_names = {}
    for name in args:
        first_letter = name[0]
        dict_names[first_letter] = dict_names.get(first_letter, []) + [name]
    return dict_names


print(thesaurus("Аркадий", "Анатолий", "Анна", "Борис", "Виталий", "Валерий", "Николай", "Сергей"))

