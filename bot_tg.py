

import telebot
from telebot import types

toKen = '5797738409:AAGzQyzbcAr8tiCoHG9h_9M6mP4vtWYuU6k'

bot = telebot.TeleBot(toKen)

cat = 'https://sun9-44.userapi.com/impf/c631117/v631117435/350da/0uCY1cnZLgQ.jpg?size=320x232&quality=96&sign=bcc2ea453c8abcd3cb15acabf8d44514&c_uniq_tag=Yx_brHEyfD3KLlV59q6GksvISu5aBH8cFH-sAULyAvk&type=album'
breathe = 'https://irkmarket.ru/images/virtuemart/product/015071.jpg'
bye = 'https://n1s1.hsmedia.ru/56/f9/39/56f939cb490775a6f3ff5077a5f67e6a/855x960_0xac120003_1794847481582807964.jpg'
banbot = 'https://telegra.ph/file/332b2d7ea6c7e72d468a5.jpg'
leavebot = 'https://mem-baza.ru/_ph/1/2/669978754.jpg?1600929977'
new = 'https://i.ytimg.com/vi/my4zV2uUF68/mqdefault.jpg'

cats = 'https://avatanplus.com/files/resources/mid/59845a36e823c15dad0066a7.png'

@bot.message_handler(commands=['start'])
def hello_message(message):
    markup = types.InlineKeyboardMarkup()
    item_1 = types.InlineKeyboardButton(text='Тык-тык', callback_data = 'cat')
    item_2 = types.InlineKeyboardButton(text='Численность чата', callback_data = 'stat')
    item_3 = types.InlineKeyboardButton(text='Бот, вам пора уйти', callback_data = 'leave')
    item_4 = types.InlineKeyboardButton(text='Котов', callback_data = 'cats')
    markup.add(item_1)
    markup.add(item_2)
    markup.add(item_3)
    markup.add(item_4)
    bot.send_message(message.chat.id,'Доброго... Что же вы хотите от меня?', reply_markup=markup)

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.send_photo(message.chat.id, new, f'Привет или здавствуйте?')

@bot.callback_query_handler(func=lambda call: True)
def message_reply(call):
    if call.data=="cat":
        bot.send_photo(call.message.chat.id, cat, 'Войдите')
    if call.data=="stat":
        users = bot.get_chat_member_count(call.message.chat.id)
        adm = bot.get_chat_administrators(call.message.chat.id)
        adm_names = []
        for n in adm:
          adm_names.append('@' + str(n.user.username))
        adm_names = ', '.join(adm_names)
        bot.send_message(call.message.chat.id, f'Количество участников: {users} \nКоличество администраторов: {len(adm)} \nАдминистраторы: {adm_names}')
    if call.data=="leave":
        bot.send_photo(call.message.chat.id, leavebot, 'Прощайте...')
        bot.leave_chat(call.message.chat.id) 
    if call.data == 'cats':
        bot.send_photo(call.message.chat.id, cats, f'Вот они слева направо...')

@bot.message_handler(commands=['to_admin'])
def handle_admin(message: types.Message):
  if bot.get_chat_member(message.chat.id, bot.user.id).status != 'administrator':
      bot.send_message(message.chat.id, f'Бот не обладает полномочиями администатора')
  elif bot.get_chat_member(message.chat.id,  message.from_user.id).status not in ['administrator', 'creator']:
      bot.send_message(message.chat.id, f'Данную команду могут вызывать только администраторы')
  elif message.reply_to_message is not None:
      name = message.reply_to_message.from_user.username
      user_id = message.reply_to_message.from_user.id
      bot.promote_chat_member(message.chat.id, user_id,
                              can_change_info = True, 
                              can_post_messages = True,
                              can_edit_messages = True, 
                              can_delete_messages = True, 
                              can_invite_users = True,
                              can_restrict_members = True, 
                              can_pin_messages = True, 
                              can_promote_members = True,
                              is_anonymous = False, 
                              can_manage_chat = True, 
                              can_manage_video_chats = True,
                              can_manage_voice_chats = True
                              )
      bot.send_message(message.chat.id,f'Наделяю @{name} властью управления 🪄')
            
@bot.message_handler(commands=['ban'])
def ban(message: types.Message):  
  if bot.get_chat_member(message.chat.id, bot.user.id).status != 'administrator':
      bot.send_message(message.chat.id,f'Бот не обладает полномочиями администатора')
  elif message.reply_to_message is not None:
      name = message.reply_to_message.from_user.username
      user_id = message.reply_to_message.from_user.id
      if name == 'halfimoon_bot': 
          bot.send_photo(message.chat.id, banbot, f'Попытка забанить бота!')
      else:
          bot.send_photo(message.chat.id, bye, f'True magic is hapenning! @{name} попал под действие бана')
          bot.ban_chat_member(message.chat.id, user_id)

@bot.message_handler(commands=['unban'])
def unban(message: types.Message):
  if bot.get_chat_member(message.chat.id, bot.user.id).status != 'administrator':
      bot.send_message(message.chat.id,f'Бот не обладает полномочиями администатора')
  elif message.reply_to_message is not None:
      name = message.reply_to_message.from_user.username
      user_id = message.reply_to_message.from_user.id
      bot.unban_chat_member(message.chat.id, user_id)
      bot.send_photo(message.chat.id, breathe, f'@{name} возвращён из бана')

@bot.message_handler(commands=['cats'])
def unban(message: types.Message):
      bot.send_photo(message.chat.id, cats, f'Вот они слева направо...')

bot.polling(none_stop=True, interval=0)
