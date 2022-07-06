import telebot

TOKEN = 'here the special private key is placed'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Hi, bruh !\nWhat do you wanna do now?\nType a command with '/'")


@bot.message_handler(commands=['all'])
def get_all(message):
    try:
        file = open('tasks.txt', 'r')
        lst = file.read().split('\n')
        if lst != ['']:
            for index, line in enumerate(lst):
                if line != '':
                    bot.send_message(message.from_user.id, str(index + 1) + '. ' + line)
        else:
            bot.send_message(message.from_user.id, 'bruh, nothing is here')
        file.close()
    except FileNotFoundError:
        bot.send_message(message.from_user.id, 'Type once more')


@bot.message_handler(commands=['new_item'])
def add_new_item(message):
    txt = message.text[10:]
    file = open('tasks.txt', 'a')
    file.write(txt + '\n')
    bot.send_message(message.from_user.id, 'Sure wanna do it?..\nkk, here is your new task: ' + txt)
    file.close()


@bot.message_handler(commands=['delete'])
def delete_item(message):
    try:
        num = int(message.text[8:]) - 1
        file = open('tasks.txt', 'r')
        lst = file.read().split('\n')
        file.close()
        if num < len(lst) - 1 and lst != ['']:
            file_w = open('tasks.txt', 'w')
            for index in range(num, len(lst) - 1):
                lst[index] = lst[index + 1]
            lst[len(lst) - 1] = ''
            for i in range(len(lst)):
                if lst[i] != '':
                    file_w.write(lst[i] + '\n')
            bot.send_message(message.from_user.id, "Success ! Task's deleted")
            file_w.close()
        else:
            bot.send_message(message.from_user.id, "No such task found, bruh")
    except ValueError:
        bot.send_message(message.from_user.id, 'Type once again')


bot.polling()
