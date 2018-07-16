# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def getNum(num, pos):
	return int(str(num)[pos]);

number = input("Введите трехзначное число ")
print("Сумма введеного числа: ", getNum(number,0) + getNum(number,1) + getNum(number,2))
print("Произведение введеного числа", getNum(number,0) * getNum(number,1) * getNum(number,2))


