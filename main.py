import telebot
import os
import logging
from dotenv import load_dotenv
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
budgets = {}
load_dotenv()

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send(message):
    logger.info("shro shod kako")
    markub = ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="Choise your opption",one_time_keyboard=True)
    markub.add(KeyboardButton('سازنده ی بازی'),KeyboardButton("بودجه من"),KeyboardButton("donate us"))
    markup = InlineKeyboardMarkup()
    game_btn = InlineKeyboardButton("بزن بریم!", callback_data="game")
    markup.add(game_btn)
    bot.send_message(
        message.chat.id,
        "سلام دوست عزیز👍\nبودجه در حال حاضر شما 30000 تومان هست و قوانین بازی به این صورت هستد\n\n1_هر بار که برنده شوید 10000 تومان برنده میشوید\n\n2_هر بار که شکست بخورید 20000 تومان میبازید\n\n3_هر وقت که بودجه شما کمتر از 10000 تومان شود شما دیگر نمیتوانید بازی کید\n\n4_هروقت که شما به بودجه 100000 تومان رسیدید میتواید گول خود را بردارید",
        reply_markup=markub
    )
    bot.send_message(
        message.chat.id,
        "اگر اماده یک بازی هیجان انگیز هستید دکمه بزن بریم را فشار دهید دهید🔥🔥🔥",
        reply_markup=markup,
        
    )

@bot.message_handler(func= lambda message: message.text =='سازنده ی بازی')
def command(message):
    chat = message.chat.id
    bot.send_message(chat,"سلام دوستان بنده ارش هستم سازنده این بات\nشما میتواند از طریغ تلگرام من با م ارتباط بگیری\nایدی من:@arash1390tqv\nامیدوارم بتونم همکاری خوبی داشته باشیم")
@bot.message_handler(func= lambda message: message.text =="بودجه من")
def command(message):
    chat = message.chat.id
    bot.send_message(chat,f"سلام دوست عزیز😁\nدر حال حاضر بودجه شما {budgets.get(message.chat.id,30000)} تومان هست\n میتوانید با بیشتر بازی کردن این مقدار را بیشتر کنید")
@bot.message_handler(func= lambda message: message.text =="donate us")
def command(message):
    chat = message.chat.id
    bot.send_message(chat,f"سلام دوست عزیز😁\nشما میتوانید با فرستادن نظر های مثبت خود به این ایدی:@arash1390tqv از ما حمایت کنید!")

@bot.callback_query_handler(func=lambda call: call.data == "game")
def game(call):
    chat = call.message.chat.id

    if chat not in budgets:
        budgets[chat] = 30000
    
    bot.send_message(
        chat,
        f"شروع کنید!(لطفا با سنگ,کاغذ و قیچی بازی کنید)\nبودجه شما: {budgets[chat]} تومان",
    )
    bot.register_next_step_handler(call.message, callback=play_game)
def play_game(message):
    while True:
        budget = budgets[message.chat.id]
        user_choice = message.text.lower()
        choices = ["سنگ", "کاغذ", "قیچی"]
        bot_choice = random.choice(choices)

        if user_choice not in choices:
            bot.send_message(
                message.chat.id,
                "لطفا فقط از گزینه های سنگ، کاغذ یا قیچی استفاده کنید.",
            )
            bot.register_next_step_handler(message, play_game)
            return

        if user_choice == bot_choice:
            result = "مساوی"
        elif (
            (user_choice == "سنگ" and bot_choice == "قیچی")
            or (user_choice == "کاغذ" and bot_choice == "سنگ")
            or (user_choice == "قیچی" and bot_choice == "کاغذ")
        ):
            result = "برنده"
            budgets[message.chat.id] += 10000
        else:
            result = "بازنده"
            budgets[message.chat.id] -= 20000

        bot.send_message(
            message.chat.id,
            f"شما {result} شدید!\nانتخاب شما: {user_choice}\nانتخاب ربات: {bot_choice}\nبودجه شما: {budgets[message.chat.id]} تومان\nمیخواهید دوباره بازی کنید؟ (لطفا با بله یا خیر پاسخ دهید)",
            
        )

        if budget < 10000:
            bot.send_message(
                message.chat.id,
                "بودجه شما کمتر از 10000 تومان است. شما دیگر نمی‌توانید بازی کنید." \
                "اگر میخواهید باز هم بازی کنید باید حساب خود را شارژ کنید و دوباره شروع کنید.",
                
            )
            return
        elif budget >= 100000:
            bot.send_message(
                message.chat.id,
                "تبریک! شما به بودجه 100000 تومان رسیدید و می‌توانید گول خود را بردارید.",
            )
            return
        bot.register_next_step_handler(message, continue_game)
        return


def continue_game(message,):
    budget = budgets[message.chat.id]
    if budget < 10000:
        bot.send_message(
            message.chat.id,
            "بودجه شما کمتر از 10000 تومان است و دیگر نمی‌توانید بازی کنید."
        )
        return

    if message.text == "بله":
        bot.send_message(
            message.chat.id,
            "بازی ادامه دارد. لطفاً سنگ، کاغذ یا قیچی را وارد کنید."
        )
        bot.register_next_step_handler(message, play_game)

    elif message.text == "خیر":
        bot.send_message(
            message.chat.id,
            f"بازی متوقف شد.\nبودجه نهایی شما: {budgets[message.chat.id]} تومان"
        )

    else:
        bot.send_message(
            message.chat.id,
            "فقط «بله» یا «خیر» وارد کنید."
        )
        bot.register_next_step_handler(message, continue_game)
bot.infinity_polling()
