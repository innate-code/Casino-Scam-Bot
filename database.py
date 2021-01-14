import numpy, datetime
import sqlite3, random, requests, string, time
import threading

from misc import repl, repl_percent, repl_share

# Misc

def project_all_payments():
	try:
		a = 0
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			rows = cur.execute("SELECT * FROM payments").fetchall()
			for row in rows:
				a += 1
		return a
	except:
		return 0

def project_all_rub():
	try:
		a = 0
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			rows = cur.execute("SELECT * FROM payments").fetchall()
			for row in rows:
				a += float(row[2])

		return round(float(a))
	except:
		return 0

def roject_all_id():
	try:
		array = []
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			rows = cur.execute("SELECT * FROM users").fetchall()
			for row in rows:
				array.append(row[1])

		return array
	except:
		return 0

# Регистрация пользователя
def user_exists_ticket(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `ticket` WHERE `user_id` = ?', (user_id,)).fetchall()
			return boot(len(result))
		except:
			return False

def user_add_ticket(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO `ticket` (`user_id`, `merchant_id`) VALUES(?,?)", (user_id, 0))
		except:
			pass

def user_exists_casino(user_id):
	try:

		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))

	except:
		return False

def user_add_casino(user_id username, invite_code):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO `users` `user_id`, `user_name`, `balance`, `invite_code`, `win`, `lose`, `all`, `receive`, `status`) VALUES(?,?,?,?,?,?,?,?,?)", (user_id, username, 0, invite_code,
				0, 0, 0, 0, 2))
	except:
		pass

# Информация о воркере