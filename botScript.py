from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

getting = {}

id_array = []

updater = Updater(token = '453302830:AAHwl5QhmhRnR0GuI5Sh4TCQk1Du8XNPvtc')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Давай общаться?')

def textMessage(bot, update):
    if (update.message.chat_id not in id_array):
        id_array.append(update.message.chat_id)
        getting[update.message.chat_id] = []
    print(getting) 
    getting[update.message.chat_id].append(update.message.text)
    if (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Triangle"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите стороны треугольника")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Triangle"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        if (a < b+c) and (b < c+a) and (c < b+a):
            bot.send_message(chat_id = update.message.chat_id, text = "Можно")
        else:
            bot.send_message(chat_id = update.message.chat_id, text = "Нельзя")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "делители"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите a ")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "делители"):
        print (100)
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        print (a)
        for i in range(1, a + 1):
            print(i)
            if a % i == 0:
                bot.send_message(chat_id = update.message.chat_id, text = str(i))
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "реши"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите a b c")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "реши"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        d = b*b - 4*a*c
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)
        res = "x1 = "+str(x1)+" x2 = "+str(x2)
        bot.send_message(chat_id = update.message.chat_id, text = res)
        

    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "закодируй"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите число для перевода")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "закодируй"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        bite = []
        biteg = []
        for i in string[0]:
            bite.append (i)
        for i in bite:
            biteg.append (bin(int(ord(i)))[2:]) 
        bot.send_message(chat_id = update.message.chat_id, text = str(biteg))

    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "декодируй"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите число для перевода")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "декодируй"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        bite = []
        biteg = []
        for i in string:
            biteg.append (chr(int(i,2)))
        string = ''.join (biteg)
        bot.send_message(chat_id = update.message.chat_id, text = str(string))
        
        a = int(ord(string[0]))
        print (a)
        b = bin(a)
        print (b)
        c = int (b, 2)
        print (c)
        d =  (c)
        print (d)
    else:
        res = 'Получил ваше сообщение: '+ update.message.text
        bot.send_message(chat_id = update.message.chat_id, text = res)

def helpp (bot,update):
    bot.send_message (chat_id = update.message.chat_id, text = "/start - начало работы; \n команды - сообщения : \n Triangle - cуществует ли треугольник с такими сторонами \n делители - все делители данного числа \n реши - решение квадратных уравнений \n закодируй - переводит текст в двоичный код \n декодируй - расшифровывает двоичный код в текст \n делители - выводит делители для целого числа")

helpp_handler = CommandHandler('help', helpp)     
start_handler = CommandHandler('start', startCommand)
text_handler = MessageHandler(Filters.text, textMessage)
                      
dispatcher.add_handler (helpp_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling(clean=True)

updater.idle()
