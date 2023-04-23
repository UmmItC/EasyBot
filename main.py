import telebot
import logging
import json
import datetime
import yaml

from telebot.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types

with open('keyboard.yaml', 'r') as f1, open('token.json', 'r') as f2:
    keyboard = yaml.safe_load(f1)
    config = json.load(f2)

locals().update(keyboard)

# getting bot token
bot_token = config['token']

# create telebot
bot = telebot.TeleBot(bot_token, parse_mode='MarkdownV2')

# setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def process_start_keyboard(message, from_back=False):
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    if not from_back:
        welcome_message = keyboard["welcome_message"].format(user_first_name=user_first_name, user_last_name=user_last_name)
    else:
        welcome_message = "你已返回主選單，請繼續使用鍵盤提供的文字輸入指令！"

    # Create keyboard
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # Create keyboard button
    stickers_btn = telebot.types.KeyboardButton('Stickers Packs')
    language_btn = telebot.types.KeyboardButton('Languages')
    bot_info_btn = telebot.types.KeyboardButton('About Bot')
    close_keyboard_btn = telebot.types.KeyboardButton('Close Keyboard')

    # adding button to keyboard
    markup.add(stickers_btn, language_btn, bot_info_btn, close_keyboard_btn)
    bot.send_message(message.chat.id, welcome_message,reply_markup=markup)

def processs_stickers_keyboard(message):
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    replykeyboard_stickers_packs = keyboard["first_keyboard_showing_message_"]["username_asking_stickers_keyboard_selected"].format(user_first_name=user_first_name, user_last_name=user_last_name)

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    Capoo_Stickerspacks_select_btn = telebot.types.KeyboardButton("Capoo Stickers Packs")
    HKG_Stickerspacks_select_btn = telebot.types.KeyboardButton("HKG Stickers Packs")
    Cute_Stickerspacks_selectbtn = telebot.types.KeyboardButton("Cute Stickers Packs")
    select_cd_back_btn = telebot.types.KeyboardButton("Back")
    close_keyboard_btn = telebot.types.KeyboardButton("Close Keyboard")

    markup.add(Capoo_Stickerspacks_select_btn, HKG_Stickerspacks_select_btn, Cute_Stickerspacks_selectbtn, select_cd_back_btn, close_keyboard_btn)
    bot.send_message(message.chat.id, replykeyboard_stickers_packs,reply_markup=markup)

def keyboard_start_if_statement(message):
    if message.chat.type == 'private':
        if message.text == "Stickers Packs":
            processs_stickers_keyboard(message)
            bot.register_next_step_handler(message,keyboard_stickers_if_statement)
        elif message.text == "Languages":
            inlinekeyboard_language_install = keyboard["first_keyboard_showing_message_"]["language_install"]
            bot.reply_to(message,inlinekeyboard_language_install)
            bot.register_next_step_handler(message,keyboard_start_if_statement)
        elif message.text == "About Bot":
            inlinekeyboard_bot_infoo = keyboard["first_keyboard_showing_message_"]["bot_infoo"]
            bot.reply_to(message,inlinekeyboard_bot_infoo)
            bot.register_next_step_handler(message,keyboard_start_if_statement)
        elif message.text == "Close Keyboard":
            bot.reply_to(message,Keyboard_close,reply_markup=ReplyKeyboardRemove())
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            location = "error_keyboard_text"
            error_keyboard_text = keyboard['Unknown_text_'][location].format(mess=message.text)
            bot.reply_to(message, error_keyboard_text)
            bot.register_next_step_handler(message,keyboard_start_if_statement)
    else:
        bot.reply_to(message,private_chat_only)
        bot.register_next_step_handler(message,keyboard_start_if_statement)

def keyboard_stickers_if_statement(message):
    if message.chat.type == 'private':
        if message.text == "Capoo Stickers Packs":
            capoo_start(message)
            bot.register_next_step_handler(message,keyboard_stickers_if_statement)
        elif message.text == "HKG Stickers Packs":
            HKG_start(message)
            bot.register_next_step_handler(message,keyboard_stickers_if_statement)
        elif message.text == "Cute Stickers Packs":
            Cute_start(message)
            bot.register_next_step_handler(message,keyboard_stickers_if_statement)
        elif message.text == "Close Keyboard":
            bot.reply_to(message,Keyboard_close,reply_markup=ReplyKeyboardRemove())
            bot.clear_step_handler_by_chat_id(message.chat.id)
        elif message.text == "Back":
            process_start_keyboard(message, from_back=True)
            bot.register_next_step_handler(message,keyboard_start_if_statement)
        else:
            location = "stickerspacks_keyboard_UK_TEXT"
            unknown_text = keyboard['Unknown_text_'][location].format(mess=message.text)
            bot.reply_to(message, unknown_text)
            bot.register_next_step_handler(message,keyboard_stickers_if_statement)
    else:
        bot.reply_to(message,private_chat_only)
        bot.register_next_step_handler(message,keyboard_stickers_if_statement)

g_Capoo_keyb = None
g_HKG_keyb = None
g_Cute_keyb = None

def capoo_inlinekeyboard():
    global g_Capoo_keyb
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    capoo_key1 = types.InlineKeyboardButton("動態 Capoo", callback_data="capoo_dynamic")
    capoo_key2 = types.InlineKeyboardButton("靜態 Capoo", callback_data="capoo_static")
    markup.add(capoo_key1, capoo_key2)
    
    # 將鍵盤賦值給全局變量 g_Capoo_keyb
    # adding keyboard variable with Global variable (g_Capoo_keyb)
    g_Capoo_keyb = markup

def HKG_inlinekeyboard():
    global g_HKG_keyb
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    hkg_key1 = types.InlineKeyboardButton("動態 HKG", callback_data="hkg_dynamic")
    hkg_key2 = types.InlineKeyboardButton("靜態 HKG", callback_data="hkg_static")
    markup.add(hkg_key1, hkg_key2)    

    g_HKG_keyb = markup

def Cute_inlinekeyboard():
    global g_Cute_keyb
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    cute_key1 = types.InlineKeyboardButton("動態 Cute", callback_data="cute_dynamic")
    cute_key2 = types.InlineKeyboardButton("靜態 Cute", callback_data="cute_static")
    markup.add(cute_key1, cute_key2)
    
    g_Cute_keyb = markup

def capoo_start(message):
    capoo_inlinekeyboard()
    keyboardcapoo_selected = keyboard["stickerspacks_keyboard_showing_message_selected_"]["select_capoo_stickers_packs"]
    bot.reply_to(message, keyboardcapoo_selected, reply_markup=g_Capoo_keyb)

def HKG_start(message):
    HKG_inlinekeyboard()
    keyboardhkg_selected = keyboard["stickerspacks_keyboard_showing_message_selected_"]["select_hkg_stickers_packs"]
    bot.reply_to(message, keyboardhkg_selected, reply_markup=g_HKG_keyb)

def Cute_start(message):
    Cute_inlinekeyboard()
    keyboardcute_selected = keyboard["stickerspacks_keyboard_showing_message_selected_"]["select_cute_stickers_packs"]
    bot.reply_to(message, keyboardcute_selected, reply_markup=g_Cute_keyb)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global Capoo_keyb
    
    if call.message:
        if call.data == "capoo_dynamic":
            bot.answer_callback_query(call.id, "即將為你顯示動態 Capoo Stickers。")
            inlinekeyboard_capoo_message_x = keyboard["inlinekeyboard_showing_message_"]["capoo_inlinekeyboard_selected_dynamic"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_capoo_message_x, reply_markup=g_Capoo_keyb)
        elif call.data == "capoo_static":
            bot.answer_callback_query(call.id, "即將為你顯示靜態 Capoo Stickers。")
            inlinekeyboard_capoo_message_x2 = keyboard["inlinekeyboard_showing_message_"]["capoo_inline_keyboard_selected_static"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_capoo_message_x2, reply_markup=g_Capoo_keyb)
        elif call.data == "hkg_dynamic":
            bot.answer_callback_query(call.id, "即將為你顯示動態 HKG Stickers。")
            inlinekeyboard_hkg_message_x = keyboard["inlinekeyboard_showing_message_"]["hkg_inline_keyboard_selected_dynamic"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_hkg_message_x, reply_markup=g_HKG_keyb)
        elif call.data == "hkg_static":
            bot.answer_callback_query(call.id, "即將為你顯示靜態 HKG Stickers。")
            inlinekeyboard_hkg_message_x2 = keyboard["inlinekeyboard_showing_message_"]["hkg_inline_keyboard_selected_static"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_hkg_message_x2, reply_markup=g_HKG_keyb)
        elif call.data == "cute_dynamic":
            bot.answer_callback_query(call.id, "即將為你顯示動態 Cute Stickers。")
            inlinekeyboard_cute_message_x = keyboard["inlinekeyboard_showing_message_"]["cute_inline_keyboard_selected_dynamic"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_cute_message_x, reply_markup=g_Cute_keyb)
        elif call.data == "cute_static":
            bot.answer_callback_query(call.id, "即將為你顯示靜態 Cute Stickers。")
            inlinekeyboard_cute_message_x2 = keyboard["inlinekeyboard_showing_message_"]["cute_inline_keyboard_selected_static"]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=inlinekeyboard_cute_message_x2, reply_markup=g_Cute_keyb)


keyboard_opened = False

@bot.message_handler(commands=['start'])
def handle_start(message):
    global keyboard_opened
    if message.chat.type == 'private':
        process_start_keyboard(message)
        bot.register_next_step_handler(message,keyboard_start_if_statement)
    else:
        bot.reply_to(message,private_chat_only)

@bot.message_handler(content_types=['sticker'])
def send_stickers(message):
    if message.chat.type == "private":
        bot.reply_to(message,"Dont send any Stickers to me.")

# setting debug mode handler
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    location = "error_dont_know"
    unknown_text = keyboard['Unknown_text_'][location].format(mess=message.text)
    bot.reply_to(message, unknown_text)
    user_info = f"*{message.from_user.first_name} {message.from_user.last_name}* with username (@{message.from_user.username}) with ID _{message.from_user.id}_"
    logging.debug(f"Received message from user {user_info} - input: {message.text}")

if __name__ == "__main__":
    bot.polling(none_stop=True)