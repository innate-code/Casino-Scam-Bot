from casino_config import bot, types in_deposit, user_status_pay, status_bot
from casino_config import user_invite_code, user_update_code, token, phone, enter_promo, bill_create, phone
from casino_config import nvuti, dice, coinflip, crash, crash_end, clear_stats, deposit, enter_receive
import casino_config, database, keyboard
import threading, time, configparser

@bot.message_handler(commands=['stats'])
def start_command(message):
	try:
		chat_id = message.chat.id
		code = message.text.split()

		if (not database.user_exists_casino(chat_id)):
			if (len(code) == 2):
				exists = database.worker_exists_code(code[1])

				if (exists is not False):
					username = message.from_user.username

					database.user_add_casino(chat_id, username, code[1])
					bot.send_message(chat_id, f"")
