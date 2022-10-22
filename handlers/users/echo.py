from aiogram import types
from loader import dp
import wikipedia
wikipedia.set_lang('uz')
print(wikipedia.search('toshkent'))
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
