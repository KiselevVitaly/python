import re


def email_parse(email):
    regexp = re.compile(r'[\w\.]+@[\w]+\.[\w\.]+')
    result = regexp.match(email)
    if result:
        return dict(zip(['username','domain'], result.group().split('@')))
    raise ValueError(f'Неверный адрес {email}')


if __name__ == '__main__':
    print(email_parse('logos_k@mail.ru'))
    print(email_parse('titov@atmosfera.msk.ru'))
    print(email_parse('test@'))
    print(email_parse('@test'))
    print(email_parse('null'))