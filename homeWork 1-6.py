# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def get_letter_by_pos(pos):
	return chr(int(pos)+96)
letter = input('Введите номер буквы ')
print(f'\nНа {letter} месте находится буква "{get_letter_by_pos(letter)}"')