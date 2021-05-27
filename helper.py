
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import string
import random

platforms = ['facebook1', 'twitter2', 'instagram3',
             'linkedin4', 'pinterest5', 'youTube6']


def select_type(platform):
    twitter2 = {'Profile_Picture': '400X400', 'landscape': '1024X512',
                'Story': '1080X1920', 'Cover_Photo': '1500X1500'}

    facebook1 = {'Profile_Picture': '170x170', 'landscape': '1200X630', 'Portrail': '630X1200',
                 'square': '1200X1200', 'Story': '1080X1920', 'Cover_Photo': '851X315'}

    instagram3 = {'Profile_Picture': '320X320', 'landscape': '1080X566',
                  'Portrail': '1080X1350', 'square': '1080X1080', 'Story': '1080X1920'}
    linkedin4 = {'Profile_Picture': '400X400', 'landscape': '1200X627',
                 'Portrail': '627X1200', 'Story': '1080X1920', 'Cover_Photo': '1128X191'}
    pinterest5 = {'Profile_Picture': '165X165', 'Board_thumbnail': '222X150'}
    youTube6 = {'Profile_Picture': '800X800',
                'Channel_cover': '2560X1440', 'Video_thumbnail': '1280X760'}

    selected_platform = eval(platform)
    markup = InlineKeyboardMarkup()
    markup.row_width = 3

    for key, value in selected_platform.items():
        markup.add(InlineKeyboardButton(key, callback_data=value))

    return markup


def select_platform():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Facebook", callback_data="facebook1"),
               InlineKeyboardButton("Twitter", callback_data="twitter2"),
               InlineKeyboardButton("Instagram", callback_data="instagram3"),
               InlineKeyboardButton("LinkedIn", callback_data="linkedIn4"),
               InlineKeyboardButton("Pinterest", callback_data="ointerest5"),
               InlineKeyboardButton("YouTube", callback_data="youTube6"),
               InlineKeyboardButton("Alternate size", callback_data="7Alternatesize"))
    return markup


def resize_again():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="yes"),
               InlineKeyboardButton("No", callback_data="no"))
    return markup


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
