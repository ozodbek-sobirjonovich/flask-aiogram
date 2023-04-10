from bg import keep_alive
from aiogram import Bot, Dispatcher, executor, types

bot = Bot("TOKEN_HERE")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def hello(message: types.Message):
    await message.reply("Hello!")

@dp.message_handler(content_types="text")
async def hello(message: types.Message):
    await message.reply(message.text)

keep_alive()
executor.start_polling(dp)