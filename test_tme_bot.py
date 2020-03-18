# TESTING HEROKU SHEDULER

import telebot
import os
import json

key = '1125207603:AAEtVfyVEVXUl6Gpi0reExeL77MP2_kakcs'
bot = telebot.TeleBot(key)

massege = 'It works!!!'

bot.send_message(chat_id='@testpingaarchannel', text=massege)
