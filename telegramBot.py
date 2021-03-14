import configparser
from aiogram import Bot, Dispatcher, executor, types
import keyboardButtonBot as kb
import imageReader as ir

# считываем конфигурационный файл
config = configparser.ConfigParser()
config.read("api.ini")

# инициализация бота
bot = Bot(token=config["API"]["API_TOKEN"])
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Начинаем работу", reply_markup=kb.greet_kb)

@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer('Нажатие кнопки')
    currentValue = ir.text
    with open(ir.name, 'rb') as photo:
        await message.answer_photo(photo, caption=currentValue)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)