list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(list):
      if s.isdigit():
            list[i] = f'"{int(s):02d}"'
      elif s[1:].isdigit():
            list[i] = f'"{s[0]}{int(s[1:]):02d}"'
      print(list[i], end=" ")
print('\n', list)
