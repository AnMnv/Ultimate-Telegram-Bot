import telegram
from typing import Union, List


import telebot 							  
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

####################
#import time

####################
from myconfig import *
bot = telebot.TeleBot(bot_key)

####################
import qrcode
####################
#import time
####################
from pytube import YouTube
####################
UserMessageID = {}
send_to_all = {}
####################
import os
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg" # for delpoy on a phone 
################### for db
import pickledb
db = pickledb.load('full_base.db', False)
usersID = pickledb.load('usersIDonly.db', False)
####################
hi_sticker = 'CAACAgIAAxkBAAEGrUxjjIc5nE63ZuwAARTGfW8SVYQJy-0AAkUDAAK1cdoGk4gQHIncDRsrBA'
pocker_face_sti = 'CAACAgIAAxkBAAEGfgNje4CHF8mJYmlBqI8UM5J-0DXg2gACDQMAAhM5jxFj1aggf1_t0isE'	# id стикерa (@idsticker_bot)	
face_hand = 'CAACAgIAAxkBAAEGvWtjkgikA_G9AAFhmIXZ7QRpr9WbN-oAArwAA5XQMAXt0_Sw87poQysE'
papei_boli = 'CAACAgIAAxkBAAEGxgNjlOk24KiISNVHEW8TOlQcICk-jQACthAAAujW4hKViMKVR2dEICsE'
####################
#import subprocess
####################
state_df = {}
####################
import matplotlib.pyplot as plt
import numpy as np
import numexpr
#################### for mp4 -> mp3
from moviepy.editor import VideoFileClip
#################### for checking webpage
import requests

#################### for dtek
import schedule
import time
import csv


@bot.message_handler(commands=['dtek1'])
def dtek1(message):
	url = "https://git.3ig.kiev.ua"
	svet_status = 1

	try:
		requests.head(f"{url}", verify=False, timeout=5)
		svet_status = 1

	except Exception as e:
		svet_status = 0
		bot.send_message(message.chat.id, "Света нету")
		bot.send_sticker(message.chat.id, papei_boli)

	with open('csv_file.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(["time", svet_status])

	time.sleep(30 * 60)
	schedule.every(5).seconds.do(dtek1(message))
	while True:
		schedule.run_pending()
		time.sleep(1)










################################################################## light check
@bot.message_handler(commands=['dtek'])
def what_link(message):
	markup =  ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	buttons = types.InlineKeyboardButton("https://git.3ig.kiev.ua") 
	markup.add(buttons)


	mes = bot.send_message(message.chat.id, "send  Your url", reply_markup=markup)
	bot.register_next_step_handler(mes, dtek)

def dtek(message):
	url = message.text
	try:
		requests.head(f"{url}", verify=False, timeout=5)
		bot.send_message(message.chat.id, "Свет есть")
	except Exception as e:
		bot.send_message(message.chat.id, "Света нету")
		bot.send_sticker(message.chat.id, papei_boli)







###################################################################	snatching user data
@bot.message_handler(commands=['start', 'menu'])
def start(message):
	bot.send_sticker(message.chat.id, hi_sticker)
	bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
	markup =  ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button_QRcode 	= types.InlineKeyboardButton("🔗 link into QR-code") 
	button_YT_video = types.InlineKeyboardButton("📥 video YouTube")
	make_it_caps = types.InlineKeyboardButton("⬆️ MAKE IT CAPS")
	plot = types.InlineKeyboardButton("📈 plot")
	mp4mp3 = types.InlineKeyboardButton("mp4 --> mp3")
	word_counter = types.InlineKeyboardButton("Word Counter")
	markup.add(button_QRcode, button_YT_video, make_it_caps, plot, mp4mp3, word_counter)
	bot.send_message(message.chat.id, """Choose what You want to do:""", reply_markup=markup)
	#write how many times user started Bot
	counter = db.get(str(f'{message.from_user.id} @{message.from_user.username} | {message.from_user.first_name} {message.from_user.last_name}'))
	usersID_counter = db.get(str(f'{message.from_user.id}'))
	if counter == False:
		db.set(str(f'{message.from_user.id} @{message.from_user.username} | {message.from_user.first_name} {message.from_user.last_name}'), '1')
		usersID.set(str(f'{message.from_user.id}'), '1')
	else:
		db.set(str(f'{message.from_user.id} @{message.from_user.username} | {message.from_user.first_name} {message.from_user.last_name}'), str(int(counter)+1))
		usersID.set(str(f'{message.from_user.id}'), str(int(usersID_counter)+1))
	db.dump()
	usersID.dump()
###################################################################	snatching user data



@bot.message_handler(content_types=['text'])
################################################################### QR-code
def commands(message):
	if 	message.text  == "🔗 link into QR-code":
		mes = bot.send_message(message.chat.id, """send a link""")
		bot.register_next_step_handler(mes, send_QRcode)
################################################################### YouTube downloader
	elif message.text == "📥 video YouTube":
		mes = bot.send_message(message.chat.id, """send a link""")
		bot.register_next_step_handler(mes, video_YouTube_download)
	elif message.text == "⬆️ MAKE IT CAPS":
		mes = bot.send_message(message.chat.id, "send a text")
		bot.register_next_step_handler(mes, make_it_caps)
	elif message.text == '📈 plot':
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
			Функция math.sin(); cos(); tan(); asin(); acos(); atan(); atan2(); hypot()."""
		bot.send_message(message.chat.id, mess1)
		mess1 = bot.send_message(message.chat.id, 'Введите функцию, типо x**2 + 5')
		bot.register_next_step_handler(mess1, plot_func)
	elif message.text == "mp4 --> mp3":
		mes = bot.send_message(message.chat.id, "send a video")
		bot.register_next_step_handler(mes, mp4mp3)
	elif message.text == "Word Counter":
		mes = bot.send_message(message.chat.id, "send message")
		bot.register_next_step_handler(mes, word_counter)


################################################################## QR-code
def send_QRcode(message):
	UserMessageID[message.text] = message.text
	data = UserMessageID[message.text]
	print("data:", data)
	img = qrcode.make(data)
	img.save('QRCode.png')
	image = open('QRCode.png', 'rb')
	bot.send_photo(message.chat.id, image)
################################################################## YouTube downloader
#def video_YouTube_download(message):
#	link = UserMessageID[message.text] = message.text
#	youtubeObject = YouTube(link)
	#youtubeObject = youtubeObject.streams.get_highest_resolution()
	#youtubeObject = youtubeObject.streams.get_lowest_resolution()
#	youtubeObject = youtubeObject.streams.filter(res="720p").first()
#	try:
#		print(link)
#		bot.send_message(message.chat.id, "Please wait, it may take some time...")
		#youtubeObject.download(filename = f"{youtubeObject.title}.mp4")
#		youtubeObject.download(filename = "qqq.mp4")
			#youtubeObject = youtubeObject.streams.get_highest_resolution().download(filename = f"{youtubeObject.title}.mp4", res="360p")
			#youtubeObject.download(filename = f"{youtubeObject.title}.mp4")
		
		 
		#bot.send_video(message.chat.id, video=open(f"{youtubeObject.title}.mp4", 'rb'))
			#os.remove(f"{youtubeObject.title}.mp4")
#	except:
#		print("Some Error!")
################################################################## text --> TEXT	
def make_it_caps(message):
	UserMessageID[message.text] = message.text
	try:
		bot.send_message(message.chat.id, message.text.upper())
	except Exception as e:
		bot.send_sticker(message.chat.id, pocker_face_sti)
		bot.send_message(message.chat.id, "Something gone wrong")
################################################################## plotting a function
def plot_func(message):
	try:
		x = np.linspace(-5,5,100)
		y = numexpr.evaluate(message.text)
		plt.plot(x, y, 'r')
		plt.savefig('qqq.png', dpi = 300)
		bot.send_photo(message.chat.id, photo=open('qqq.png', 'rb'))
		os.remove('qqq.png')
	except Exception as e:
		bot.send_sticker(message.chat.id, pocker_face_sti)
		bot.send_message(message.chat.id, "Something gone wrong")


################################################################## mp4 --> mp3
@bot.message_handler(content_types=['video'])
def mp4mp3(message):
	try:
		video = bot.get_file(message.video.file_id)
		video_name = message.video.file_name
		video_path = video.file_path
		video_as_file = bot.download_file(video_path)
		with open(video_name, "wb") as videofile:
			videofile.write(video_as_file)

		clip = VideoFileClip(video_name)
		clip.audio.write_audiofile(f'{video_name}.mp3')
		clip.close()

		with open(f'{video_name}.mp3', 'rb') as audio:
			bot.send_audio(message.from_user.id, audio)
		audio.close()

	except Exception as e:
		bot.send_sticker(message.chat.id, face_hand)
		bot.send_message(message.chat.id, "Size of video is too big")

################################################################## word counter
def word_counter(message):
	try:
		words = len(message.text.split())
		bot.send_message(message.chat.id, words)
	except Exception as e:
		bot.send_sticker(message.chat.id, pocker_face_sti)
		bot.send_message(message.chat.id, "Something gone wrong")
































############################ message to all users
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
			markup = types.InlineKeyboardMarkup()
			b1 = types.InlineKeyboardButton("Заказать слона", url="https://github.com/AnMnv/AnMnv")
			markup.add(b1)
			keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			bot.send_message(i, send_to_all[message.from_user.id], reply_markup=markup)
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


#@bot.message_handler(commands=['send'])
#def send(message):
#	bot.send_message(262330332, 'Ку-ку')
################################################################################----------------
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
	send_to_all[message.text] = message.text

def send_all_users(message):
	if message.text == "Да":
		for i in usersID.getall():
			bot.send_message(i, send_to_all[message.text])
############################





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
#@bot.message_handler(content_types=['text'])
#def plot(message):
#	if message.text == 'график 📈':
#		mess1 = """
#			Целочисленное деление двух чисел: "//"\n
#			Возведение в степень: "**"\n
#			Получение остатка от деления: "%"\n
#			ceil() и floor() — целая часть числа\n
#			fabs() — абсолютное значение\n
#			factorial() — функция факториала\n
#			fmod() — остаток от деления\n
#			frexp()\n
#			fsum() — точная сумма float\n
#			Функции возведения в степень и логарифма\n
#			exp(); expm1()\n
#			log() — логарифм числа\n
#			log1p(); log10()\n
#			pow() – степень числа\n
#			sqrt() — квадратный корень числа\n
#			Тригонометрические функции\n
#			Функция math.sin(); cos(); tan(); asin(); acos(); atan(); atan2(); hypot().
#				"""
#		bot.send_message(message.chat.id, mess1)
#		mess1 = bot.send_message(message.chat.id, 'Введите функцию, типо x**2 + 5')#, reply_markup=rmk)
#		bot.register_next_step_handler(mess1, plot_func)




###############################   plotting    #######################################
#def plot_func(message):
#	try:
#		x = np.linspace(-5,5,100)
#		y = numexpr.evaluate(message.text)
#		plt.plot(x, y, 'r')
#		plt.savefig('plot_name.png', dpi = 300)
#		bot.send_photo(message.chat.id, photo=open('plot_name.png', 'rb'))
#	except Exception as e:
#		bot.send_message(message.chat.id, f'Сам {message.text}')










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

 





######################  одобрить/удалить ###############################








bot.polling(none_stop=True)

######################### for making only project requirements
#pip install pipreqs
#pipreqs test_bot.py


















 