# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
start = input('Введите первую букву ')
end = input('Введите вторую букву ')
def get_abc_pos(letter):
	return ord(letter)-96
print(f'\nБуква "{start}" в алфавите на {get_abc_pos(start)} месте\nБуква "{end}" в алфавите на {get_abc_pos(end)} месте\nМежду ними {get_abc_pos(end)-get_abc_pos(start)-1} букв')
