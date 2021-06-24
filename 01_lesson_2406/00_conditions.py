'''
if выражение:
--->действие_1
else:
--->действие_2
'''

n = int(input('Введите четное число больше 10: '))

if n > 10 and n % 2 == 0:
    print('OK')
else:
    print('Условия не соблюдены!')

users = {
    'email': 'zodiac@gmail.com',
    'password': '12345qwerty'
}

login = input('Login: ').lower()
password = input('Password: ')

if login in users['email'] and password in users['password']:
    print('Welcome')
else:
    print('Incorrect login and/or password')
