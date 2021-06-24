phone = '+375 (29) 345-12-78'
clear_number = ''
restricted = '+-() '

for symbol in phone:
    if symbol not in restricted:
        clear_number += symbol

print(clear_number)



