from aiogram.utils.exceptions import BotBlocked
import asyncio
import logging
import time
import os
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from aiogram.utils.callback_data import CallbackData
import text_1



TOKEN = '5442548683:AAEFOLHw6zehWzMD8qTk8c9EEkWb-aUrP6o'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)
###########################################
start_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
start_b = KeyboardButton('Дізнатися що може бот.')
start_kb.add(start_b)
@dp.message_handler(lambda message: message.text == "Дізнатися що може бот.")
async def back(message: types.Message):
     await message.answer('тут /help або опис всіх команд\n /перша_допомога\n\
/псих_допомога\n\
/опізнати_загрозу\n ',reply_markup=ReplyKeyboardRemove())
####################клава старт#########################
aidkit_b = KeyboardButton('Аптечка')
firstaid_b = KeyboardButton('Перша допомога')
mines_b = KeyboardButton('Міни')
keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
keyboard_2.add(aidkit_b,firstaid_b,mines_b)


starting_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
start_kb.add()


########клавіатура для опізнавання##########
art_b = KeyboardButton('Артилерія')
rock_b = KeyboardButton('Ракета')
ppo_b = KeyboardButton('ППО')
plane_b = KeyboardButton('Літак')
grad_b = KeyboardButton('Град чи Смерч')
keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
keyboard_1.add(art_b,rock_b,ppo_b,plane_b,grad_b)
#################вихід опізнавання#######################
kbonereply = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
back_b = KeyboardButton('Повернутися')
exit_b = KeyboardButton('Вихід')
kbonereply.add(back_b,exit_b)
@dp.message_handler(lambda message: message.text == "Повернутися")
async def back(message: types.Message):
     await message.answer("Виконую:",reply_markup=keyboard_1)
@dp.message_handler(lambda message: message.text == "Вихід")
async def back(message: types.Message):
     await message.answer("Успіх:",reply_markup=ReplyKeyboardRemove())
####################вихід міни##################
kbback= ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
back1_b = KeyboardButton('Назад')
exit1_b = KeyboardButton('Вийти')
kbback.add(back1_b,exit1_b)
@dp.message_handler(lambda message: message.text == "Назад")
async def back(message: types.Message):
     await message.answer("Виконую:",reply_markup=mines_kb)
@dp.message_handler(lambda message: message.text == "Вийти")
async def back(message: types.Message):
     await message.answer("Успіх:",reply_markup=ReplyKeyboardRemove())
###############міни клавіатура#######################
fugas_b = KeyboardButton('На пелюстку')
oskolk_b = KeyboardButton('На циліндр')
tank_b = KeyboardButton('Вона велика і кругла')
other_b = KeyboardButton('Інше шось')
mines_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
mines_kb.add(fugas_b,oskolk_b,tank_b,other_b)
########клавіатура для надання першої допомоги##########

###############клава для аптечки######################
medkit_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
emergency_b = KeyboardButton('Що має бути ?')
emergency2_b = KeyboardButton('Що можна взяти ?')
toknow_b = KeyboardButton('Правила складання')
fordoc_b = KeyboardButton('Що взяти доктору ?')
medkit_kb.add(emergency_b,emergency2_b,toknow_b,fordoc_b)
####################клава для першої допомоги####################
firstaid_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
name_b = KeyboardButton(text)
name2_b = KeyboardButton(text)
name3_b = KeyboardButton(text)
name4_b = KeyboardButton(text)
firstaid_kb.add(name_b,name2_b,name3_b,name4_b)
#######psy_help#########
l_tb = (InlineKeyboardButton(url ='https://golovanivsk.crl.org.ua/news/1630485647/',text='Перейти на сайт'))
h_tb = (InlineKeyboardButton(text="Перейти на сайт",url="https://ru-ru.facebook.com/centr.serdenko/"))
life_tb = (InlineKeyboardButton(text='Перейти на сайт',url='https://lifelineukraine.com/'))
l_t = InlineKeyboardMarkup().add(l_tb)
h_t = InlineKeyboardMarkup().add(h_tb)
life_t = InlineKeyboardMarkup().add(life_tb)
lets_talk = ['"Давай поговоримо"',"0-800-331-800","12:00-22:00",'national@redcross.org.ua']
heart = ['Центр психологічної допомоги "Серденько"','067-888-75-13','цілодобово','centr.serdenko@ukr.net']
lifeline = ['"Lifeline Ukraine"','7333','цілодобово','info@lifelineukraine.com']
info_psy_b = (ReplyKeyboardMarkup())
@dp.message_handler(commands='псих_допомога')
async def psy_com1(message=types.Message):
    await message.answer(f"Підтримка від:\n{lets_talk[0]} \nНомер: {lets_talk[1]} \nГодини роботи: {lets_talk[2]}\nEmail: {lets_talk[3]}  ", reply_markup=(l_t))
    time.sleep(1)
    await message.answer(f"Підтримка від:\n{heart[0]} \nНомер: {heart[1]} \nГодини роботи: {heart[2]}\nEmail: {heart[3]}  ", reply_markup=(h_t))
    time.sleep(1)
    await message.answer(f"Підтримка від:\n{lifeline[0]} \nНомер: {lifeline[1]} \nГодини роботи: {lifeline[2]}\nEmail: {lifeline[3]}  ", reply_markup=(life_t))
    await message.answer("Бажаєте отримати інформацію як допомогти собі самостійно ?",reply_markup=info_psy)
# #############розпізнавання#############
@dp.message_handler(commands=['опізнати_загрозу'])
async def op_keyboard(message: types.Message):
     await message.reply("Оберіть предмет опізнавання:", reply_markup=keyboard_1)  
#хендлери опізнавальних кнопок#
@dp.message_handler(lambda message: message.text == "Артилерія")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\art.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.art,parse_mode= 'Markdown',reply_markup = kbonereply)
@dp.message_handler(lambda message: message.text == "Ракета")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\rocket.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.rocket,parse_mode= 'Markdown',reply_markup = kbonereply)     
#add photo
@dp.message_handler(lambda message: message.text == "ППО")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\ppo.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.ppo,parse_mode= 'Markdown',reply_markup = kbonereply)     
@dp.message_handler(lambda message: message.text == "Літак")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\plane.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.plane,parse_mode= 'Markdown',reply_markup = kbonereply)     
@dp.message_handler(lambda message: message.text == "Град чи Смерч")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\grad.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.grad,parse_mode= 'Markdown',reply_markup = kbonereply)     
################перша допомога####################
@dp.message_handler(commands=['перша_допомога'])
async def op_keyboard(message: types.Message):
     await message.reply("Оберіть розділ:", reply_markup=keyboard_2)  

@dp.message_handler(lambda message: message.text == "Аптечка")
async def aidkit(message: types.Message):
     await message.reply("Оберіть розділ:", reply_markup=medkit_kb)

#aid kit handlers # треба імена і підписи
@dp.message_handler(lambda message: message.text == "Що має бути ?")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\kit1.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= 'Дане фото демонструє список важливих речей в аптечці:',parse_mode= 'Markdown',reply_markup = ReplyKeyboardRemove())     

@dp.message_handler(lambda message: message.text == "Що можна взяти ?")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\kit2.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= 'Ці речі бажано мати в своїй аптечці:',parse_mode= 'Markdown',reply_markup = ReplyKeyboardRemove())     

@dp.message_handler(lambda message: message.text == "Правила складання")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\kit3.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= 'Правила складання аптечки на фото:',parse_mode= 'Markdown',reply_markup = ReplyKeyboardRemove())     

@dp.message_handler(lambda message: message.text == "Що взяти доктору ?")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\kit4.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= 'Людина з навичками може взяти наступне:',parse_mode= 'Markdown',reply_markup = ReplyKeyboardRemove())     

#########first aid handlers##########



#################міни####################
@dp.message_handler(lambda message: message.text == "Міни")
async def mine(message: types.Message):
     await message.answer(text_1.mines,parse_mode= 'Markdown')
     await message.answer("Якщо ви бачите підозрілі об\'єкти - відійдіть на 300 метрів та обов\'язково повідомте відповідні органи.\nНічого не чіпайте!")
     await message.reply("На що вона схожа:", reply_markup=mines_kb)  

@dp.message_handler(lambda message: message.text == "На пелюстку")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\pel.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.pel,parse_mode= 'Markdown',reply_markup = kbback)
@dp.message_handler(lambda message: message.text == "На циліндр")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\zil.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.zil,parse_mode= 'Markdown',reply_markup = kbback)
@dp.message_handler(lambda message: message.text == "Вона велика і кругла")
async def unrev(message: types.Message):
     photo = open('C:\\Users\\Asus\\Desktop\\Papka\\Photo\\big.jpg', 'rb')
     await bot.send_photo(chat_id=message.chat.id,photo=photo,caption= text_1.big,parse_mode= 'Markdown',reply_markup = kbback)    
@dp.message_handler(lambda message: message.text == "Інше")
async def unrev(message: types.Message):
     await message.answer("Це можуть бути:",reply_markup=mines_kb)
     time.sleep(0.3)
     await message.answer(text_1.unbom)  
     time.sleep(0.3) 
     await message.answer(text_1.samorob)   
     time.sleep(0.3)       #Нерозірвані боєприпаси Саморобні вибухові  
#################################
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')    
    await message.reply(f"Привіт {user_full_name}, тебе вітає бот Є-Підмога",reply_markup=start_kb)     


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_name = message.from_user.first_name
    logging.info(f'{user_name}'' used help')
    await message.answer('''
    опис бота
    opis
    opis
    opis
    opis
    ''')

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"User blocked bot!\nMessage: {update}\nException: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
