import telegram
from typing import Union, List


import telebot 							  
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

####################
import time

bot = telebot.TeleBot('1147204820:AAH54bhdtDSuCmXRi5bq9XGbWcxzAbMYlzo')

send_to_all = {}

####################
import qrcode

####################
import time

 








#@bot.message_handler(commands=['send'])
#def send(message):
#	bot.send_message(262330332, 'Ку-ку')
################################################################################
last_time = {}
 
@bot.message_handler(commands=['menu'])
def message_handler(message):
    if message.chat.id not in last_time:
        last_time[message.chat.id] = time.time()
    else:
        if (time.time() - last_time[message.chat.id]) * 1000 < 500:
            return 0
        last_time[message.chat.id] = time.time()
 
################################################################################https://www.cyberforum.ru/python-api/thread2722383.html














############################
@bot.message_handler(commands=['sendallfromadminqqq'])
def send(message):
	msg1 = bot.send_message(message.chat.id, 'Введи текст который нужно отправить всем')
	bot.register_next_step_handler(msg1, send_all)

def send_all(message):
	rmk = ReplyKeyboardMarkup(row_width=2,one_time_keyboard=True,resize_keyboard=True)
	rmk.add(InlineKeyboardButton("Да"), InlineKeyboardButton("Нет"))
	msg1 = bot.send_message(message.chat.id, 'Отправить?', reply_markup=rmk)
	bot.register_next_step_handler(msg1, send_all_users)
	send_to_all[message.from_user.id] = message.text

def send_all_users(message):
	if message.text == "Да":
		for i in usersID.getall():
			bot.send_message(i, send_to_all[message.from_user.id])
############################




















@bot.message_handler(commands=['bio'])
def bio(message):
	markup =  types.InlineKeyboardMarkup(row_width=1)

	button_github 		= types.InlineKeyboardButton("🌟 My Github 🌟", url="https://github.com/AnMnv/AnMnv")
	button_mems 		= types.InlineKeyboardButton("Channel with mems 🤡", url="https://t.me/topEverydayMem")
	button_music 		= types.InlineKeyboardButton("Channel with music 🎧", url="https://t.me/drop_trap")
	button_projects 	= types.InlineKeyboardButton("Cool open resource projects 🔥", url="https://t.me/MyOpenSourceList")

	markup.add(button_github,button_mems,button_music,button_projects)
	bot.send_message(message.chat.id, """Hello! I'm WinnieNotThePooh\nHere are some of my projects:""", reply_markup=markup)





############################	QR-code	############################
@bot.message_handler(commands=['menu'])
def menu(message):
	markup =  ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	button_QRcode = types.InlineKeyboardButton("link into QR-code")
	markup.add(button_QRcode)
	bot.send_message(message.chat.id, """Choose what You want to do:""", reply_markup=markup)


#data = 'QR Code using make() function'

########################################################
@bot.message_handler(content_types=['text'])
def commands(message):
	if message.text == "link into QR-code":
		mes = bot.send_message(message.chat.id, """send a link""")
		bot.register_next_step_handler(mes, send_QRcode)
def send_QRcode(message):
		data = f'{message.text}'
		img = qrcode.make(data)
		img.save('QRCode.png')
		image = open('QRCode.png', 'rb')
		bot.send_photo(message.chat.id, image)








############################	buttons	Разраб	############################
@bot.message_handler(commands=['qqq'])
def website(message):
	markup = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton("👉 Бот 👈", url="https://t.me/mynessbot")
	markup.add(b1)
	keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bot.send_message(message.chat.id, """Приветствуем всех""", reply_markup=markup)

########################################################

#######################     plotting a function      ##############################
@bot.message_handler(content_types=['text'])
def plot(message):
	if message.text == 'график 📈':
		mess1 = """
			Целочисленное деление двух чисел: "//"\n
			Возведение в степень: "**"\n
			Получение остатка от деления: "%"\n
			ceil() и floor() — целая часть числа\n
			fabs() — абсолютное значение\n
			factorial() — функция факториала\n
			fmod() — остаток от деления\n
			frexp()\n
			fsum() — точная сумма float\n
			Функции возведения в степень и логарифма\n
			exp(); expm1()\n
			log() — логарифм числа\n
			log1p(); log10()\n
			pow() – степень числа\n
			sqrt() — квадратный корень числа\n
			Тригонометрические функции\n
			Функция math.sin(); cos(); tan(); asin(); acos(); atan(); atan2(); hypot().
				"""
		bot.send_message(message.chat.id, mess1)
		mess1 = bot.send_message(message.chat.id, 'Введите функцию, типо x**2 + 5')#, reply_markup=rmk)
		bot.register_next_step_handler(mess1, plot_func)




###############################   plotting    #######################################
def plot_func(message):
	try:
		x = np.linspace(-5,5,100)
		y = numexpr.evaluate(message.text)
		plt.plot(x, y, 'r')
		plt.savefig('plot_name.png', dpi = 300)
		bot.send_photo(message.chat.id, photo=open('plot_name.png', 'rb'))
	except Exception as e:
		bot.send_message(message.chat.id, f'Сам {message.text}')










############################	что умее этот бот	############################
def website(message):
	markup = types.InlineKeyboardMarkup()
	button = types.InlineKeyboardButton("Delete", callback_data='Delete')#, bot.send_message(message.chat.id, """Приветствуем всех"""))
	markup.add(button)
	keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bot.send_message(message.chat.id, """Приветствуем всех""", reply_markup=markup)
	#bot.send_message(message.chat.id, "Delete")

#def delete_mes(contents=['text']):
#	if message.text == 'Delete':
#		bot.delete_message(message.chat.id, message.message_id + 1)

 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Delete":
       bot.answer_callback_query(call.id, "Эт хорошо.")
       bot.send_message(call.message.chat.id, "Эт хорошо.")




######################  одобрить/удалить ###############################








bot.polling(none_stop=True)




















 