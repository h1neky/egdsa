from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnVpr = InlineKeyboardButton(text="❓Спросить(Попросить)/Ask❓", callback_data="generateask")
btnImg = InlineKeyboardButton(text="✨Сгенерировать Изображение/Generate An Image✨", callback_data="generateimg")

Menu = InlineKeyboardMarkup(row_width=1)
Menu.insert(btnVpr)
Menu.insert(btnImg)

ProfileAsk = KeyboardButton('❓Спросить(Попросить)/Ask❓')
ProfileImg = KeyboardButton('✨Сгенерировать Изображение/Generate An Image✨')
ProfileDonate = KeyboardButton('💸Поддержать Автора/Support the Author💸')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(ProfileAsk, ProfileImg, ProfileDonate)