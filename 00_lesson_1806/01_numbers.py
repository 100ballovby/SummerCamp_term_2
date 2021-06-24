import math


num1 = float(input('Give me a number: '))  # -> str()
num2 = float(input('Give me a number: '))
# input() - позволяет ввести что-то с клавиатуры

add = num1 + num2
div = num1 / num2
mult = num1 * num2
print(math.floor(add), math.ceil(div), mult)
# floor(x) <- округляет x в меньшую сторону
# ceil(x) <- округляет x в большую сторону

