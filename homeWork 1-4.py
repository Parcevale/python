# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
def r_num(start,end):
	return random.randint(int(start),int(end))

def r_float(start,end,length=2):
	return round(random.uniform(float(start),float(end)),length)

def r_symbol(start,end):
	return chr(r_num(ord(start),ord(end)))

core = {'n': r_num, 'f': r_float, 's': r_symbol}

enter_text = 'Для получения случайного числа введите n\nДля получения случайного вещественного числа введите f\nДля получения случайного символа введите s\n'
choice = input(enter_text)
result = core[choice](
	input('Введите минимальное значение '),
	input('Введите максимальное значение ')
)
print(result)