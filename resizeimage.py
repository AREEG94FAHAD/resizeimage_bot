import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import content_type_media
from PIL import Image
from .helper import select_platform, resize_again, platforms, get_random_string, select_type

APITOKENRESIZE = os.environ.get('APITOKENRESIZE')

bot = telebot.TeleBot(APITOKENRESIZE)
sizee = {}
sizee['width'] = ''
sizee['height'] = ''


@bot.message_handler(commands=['start'])
def send_welcome(message):
    sizee['width'] = ''
    sizee['height'] = ''
    msg = bot.send_message(
        message.chat.id, "Select one", reply_markup=select_platform())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    sizee['width'] = ''
    sizee['height'] = ''

    try:
        if call.data in platforms:
            bot.send_message(call.from_user.id, "Select one",
                             reply_markup=select_type(call.data))

        elif call.data == "7Alternatesize":

            bot.send_message(call.from_user.id, "Send the width")
        elif call.data == 'yes':
            bot.send_message(call.from_user.id, "Select one",
                             reply_markup=select_platform())
        elif call.data == 'no':
            bot.send_message(call.from_user.id, "Ok no problem")
        else:
            sizee['width'], sizee['height'] = call.data.split('X')
            bot.send_message(call.from_user.id, "Send the Image ")


    except:
        bot.send_message(call.from_user.id,
                         'something went wrong try again later')


@bot.message_handler(func=lambda message: True)
def message_handler(message):

    try:
        if message.text.isnumeric():
            if int(message.text) > 3000:
                bot.send_message(message.chat.id, 'Must be between 1 to 2999')
            elif sizee['width'] == '':
                sizee['width'] = message.text
                bot.send_message(message.chat.id, 'Send the height')
            elif sizee['width'] != '' and sizee['height'] == '':
                sizee['height'] = message.text
                bot.send_message(message.chat.id, 'Send the Image')

        else:
            bot.send_message(message.chat.id, "Select one",
                             reply_markup=select_platform())

    except:
        bot.send_message(
            message.chat.id, 'Something went wrong try agin later')


@bot.message_handler(content_types=content_type_media)
def image_handler(message):
    try:

        if sizee['width'] == '' or sizee['height'] == '':
            bot.send_message(message.chat.id, "Send the Width")
        
        else:
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            imageName = get_random_string(16)
            with open(imageName+".jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, '10 second left ')
            image = Image.open(imageName+".jpg")

            new_image = image.resize((int(sizee['width']), int(sizee['height'])))
            new_image.save(imageName+".jpg")
            bot.reply_to(message, '5 second left ')
            chat_id = message.chat.id
            doc = open(imageName+".jpg", 'rb')
            bot.send_document(chat_id, doc)
            doc.close()

            sizee['width'] = ''
            sizee['height'] = ''
            bot.reply_to(message, ' Thank you for useing this bot do want to use it again',
                        reply_markup=resize_again())
            os.remove(imageName+".jpg")
    except:
        bot.send_message(message.chat.id,'Something went wrong try again later')

bot.polling()
