import aiogram
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image, ImageDraw
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from decimal import Decimal
import openai
import loguru
from loguru import logger
from aiogram import Bot, types
import markups as nav

storage = MemoryStorage()

class Form(StatesGroup):
    start = State()
    start1 = State()

openai.api_key = "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"

logger.add("debug.log")
# Initialize bot
bot = aiogram.Bot(token="6049996039:AAHkXlaJzOM6MHa40IaKocCq1A7BPWF0X08")
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Привет это бот ИИ который сможет помочь тебе с любым вопрос на разный языках! Просто выбери на кнопках или клавиатуре то что тебе нужно;)\n\nHi, this is an AI bot that can help you with any question in different languages! Just select what you need on the buttons or keyboard;)\n\nБот сделан @hnkych | Bot created @hnkych", reply_markup=nav.mainMenu)

@dp.message_handler()
async def users(message: types.Message):
            
    if message.text in ["❓Спросить(Попросить)/Ask❓"]:
        await Form.start1.set()
        await bot.send_message(message.from_user.id, "♻️Напиши свой запрос/Write your request♻️")

    if message.text in ["✨Сгенерировать Изображение/Generate An Image✨"]:
        await Form.start.set()
        await bot.send_message(message.from_user.id, "♻️Напиши свой запрос/Write your request♻️")
    
    if message.text in ["💸Поддержать Автора/Support the Author💸"]:
        await bot.send_message(message.from_user.id, f"Привет. Так как мой бот никак не приносит мне прибыли и для вас он совершенно бесплатно.\nВ моём боте неограниченное количество запросов и нет рекламы. Но сами api ключи для бота приобретаются мною за мои деньги, поэтому я решил создать такую кнопку.\nЕсли вы хотите поддержать проект то реквизиты для отправки денег ниже. Я никого не заставляю платить, вы решаете сами поддержать меня или нет, а можете просто написать мне спасибо @hnkych\n\nРеквизиты:\n QIWI: https://qiwi.com/n/H1NEKY\n VISA CARD: <code>4890 4947 9930 5347</code>\n MIR CARD: <code>2200 7302 4024 4190</code>\nЗаранее спасибо ;)", parse_mode='html')

@dp.message_handler(state=Form.start)
async def process_name_step(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    await bot.send_message(message.from_user.id, "Подожди пару секунд, бот генерирует ответ❤️\n\nWait a couple of seconds, the bot writes an answer❤️")
    response = openai.Image.create(
        prompt=message.text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    await message.reply_photo(photo=image_url)
    logger.info(f"Пользователь @{user_name} / {user_id} Отправил запрос на фото: {text}")
    await state.finish()


@dp.message_handler(state=Form.start1)
async def process_name_step1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    await bot.send_message(message.from_user.id, "Подожди пару секунд, бот генерирует ответ❤️\n\nWait a couple of seconds, the bot writes an answer❤️")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=4048,
        n=1,
        stop=None,
        temperature=1,
    )
    await message.reply(response.choices[0].text + "\n\nБот сделан @hnkych | Bot created @hnkych", reply_markup=nav.mainMenu)

    logger.info(f"Пользователь @{user_name} / {user_id} Отправил запрос : {text}")
    await state.finish()


    
    


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)