from telebot import TeleBot, types

token = "5875690739:AAFzdcAH4fB4h0VNVv9r9kiKTG2_QrNmOqE"
mybot = TeleBot(token)


@mybot.message_handler(commands=['start'])
def boshlash(message):
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Matematika", callback_data="MA")
    button2 = types.InlineKeyboardButton("Fizika", callback_data="FI")
    button3 = types.InlineKeyboardButton("Ingliz tili", callback_data="EN")
    buttons.add(button1)
    buttons.add(button2)
    buttons.add(button3)

    mybot.send_message(message.chat.id, "Sizga qaysi fan kerak: ", reply_markup=buttons)


@mybot.callback_query_handler(func=lambda call: True)
def tugma_bosildi(call):
    user_id = call.message.chat.id
    if call.data == "MA":
        mybot.delete_message(user_id, call.message.id)
        mybot.send_message(user_id, "Matematika kursi haqida malumot:\n Narxi: 300 ming so'm\n Davomiyligi: Haftada 8soat")

    elif call.data == "FI":
        mybot.delete_message(user_id, call.message.id)
        mybot.send_message(user_id, "Matematika kursi haqida malumot:\n Narxi: 300 ming so'm\n Davomiyligi: Haftada 8soat")

    elif call.data == "EN":
        mybot.delete_message(user_id, call.message.id)
        mybot.send_message(user_id, "Matematika kursi haqida malumot:\n Narxi: 300 ming so'm\n Davomiyligi: Haftada 8soat")

def begin(message):
    buttonn = types.ReplyKeyboardMarkup()
    buttonn.row("Kursga qatnashish")
    mybot.send_message("Telefon raqamingizni qoldiring siz bilan albatta bog'lanamiz", reply_markup=buttonn)
mybot.polling()