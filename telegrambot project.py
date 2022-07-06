import telebot
import sqlite3
import logging
from db_queries import *

bot = telebot.TeleBot('1313925249:AAHW_Xm0SyzXw7nYIpzcFzzR1dcSsHWq9g8', parse_mode=None)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

conn = sqlite3.connect('tg.bd')


def init_db(conn=conn, force: bool = True):
    cursor = conn.cursor()
    if force:
        cursor.execute('DROP TABLE IF EXISTS users')

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
             id INTEGER AUTO_INCREMENT,
             user_id INT,
             task_id INT,
             tasks TEXT)""")
    conn.commit()


init_db()


@bot.message_handler(commands=['start'])
def start_command(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,
                         "Hi, bruh !\nWhat do you wanna do now?\nType a command with '/'")
    else:
        bot.send_message(message.from_user.id, 'Type /start')


@bot.message_handler(commands=['new_item'])
def new_item_command(message):
    user_id = message.from_user.id
    task = message.text[9:]
    db_new_task(conn, user_id, task)
    bot.send_message(message.from_user.id, 'SURE task is saved')
    list_all_command(message)


@bot.message_handler(commands=['delete'])
def delete_command(message):
    user_id = message.from_user.id
    task_id = int(message.text[7:])
    db_delete(conn, user_id, task_id)
    bot.send_message(message.from_user.id, 'Task is deleted')


@bot.message_handler(commands=['all'])
def list_all_command(message):
    user_id = message.from_user.id
    tasks = db_take_all(conn, user_id)
    for task in tasks:
        bot.send_message(message.from_user.id, task)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    # init_db()
