from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6372658483:AAGWHb_55-eymzEVwFjB20xzg8cd4B8UJ9c')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть страницу', web_app=WebAppInfo(url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')))
    await message.answer('Привет!', reply_markup=markup)



executor.start_polling(dp)

