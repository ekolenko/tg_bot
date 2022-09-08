from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5407304437:AAHiAugKKNrhHTtws17-OewjdfgRyepTSCk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text='Привет')

@dp.message_handler(text=['привет1'])
async def answer_prvt_text(message: types.Message):
    await message.answer(text='+')

executor.start_polling(dp)
