# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
lst = [a,b,c]
long_side = max(lst)
print('long side', long_side)
lst.remove(long_side)
if sum(lst) > long_side :
	print("трегольник существует")
else :
	print("Треугольника не существует")