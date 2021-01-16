from telebot import types

# Клавиатура основная
def main_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Мой профиль')
	btn2 = types.KeyboardButton('Меню')
	btn3 = types.KeyboardButton('О проекте')
	markup.add(btn1, btn2)
	markup.add(btn3)

	return markup

# Клавиатура завершения игры
def clear_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Завершить игру')
	markup.add(btn1)
	
	return markup

# Клавиатура казино
def casino_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Играть')
	btn4 = types.KeyboardButton('Тех. Поддержка')
	btn5 = types.KeyboardButton('Личный кабинет')
	markup.add(btn1)
	markup.row(btn4, btn5)

	return markup

def game_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Random Number')
	btn2 = types.KeyboardButton('Dice')
	btn3 = types.KeyboardButton('Орел & Решка')
	btn4 = types.KeyboardButton('Crash')
	btn5 = types.KeyboardButton('Назад')
	markup.add(btn1, btn2)
	markup.row(btn3, btn4)
	markup.add(btn5)

	return markup

# Nvuti клавиатура
def nvuti_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('> 50')
	btn2 = types.KeyboardButton('= 50')
	btn3 = types.KeyboardButton('< 50')
	markup.add(btn1, btn2, btn3)

	return markup

# Coinflip клавиатура
def crash_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Орел')
	btn2 = types.KeyboardButton('Решка')
	markup.add(btn1, btn2)

	return markup

# Crash клавиатура
def crash_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Остановить график')
	markup.add(btn1)

	return markup

# Back клавиатура
def back_keyboard();
	markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
	btn1 = types.KeyboardButton('Назад')
	markup.add(btn1)

	return markup