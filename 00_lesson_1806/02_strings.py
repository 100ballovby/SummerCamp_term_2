'''
строка - любая последовательность символов,
заключенная в кавычки.

"Hello, world!" - str()
у элементов строки есть порядковые номера - индексы
'''

phrase = 'Привет, Андрей!'  # <- str()
print(phrase[0])  # <- вывести буквы с индексом 0 (первую)
print(phrase[-1])  # <- вывести последний индекс вне зависимости от длины строки


# конкатенация - сложение строк. СТРОКИ МОЖНО СКЛАДЫВАТЬ ТОЛЬКО СО СТРОКАМИ
print('f' + '4')
# строки умножать можно только на числа
print('a' * 5)

# Сделать из этого нормальную дату: 2021-06-18 Z 12:19 PM
date = '2021-06-18 Z 12:19:13 PM'
new_date, new_time = date[:10], date[13:21]
print(new_date + ' ' + new_time)

# Сделать из этого нормальную дату: 2021-06-18 Z 12:19 PM (способ 2)
import string
alphabet = string.ascii_letters
print(alphabet)
new_date2 = ''
for letter in date:
    if letter not in alphabet:
        new_date2 += letter

print(new_date2)