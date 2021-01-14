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