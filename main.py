import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7111707138:AAHSYS3cItGMHRTMS9zFiwjacLmPcFgZ_ag"

dp = Dispatcher()

check = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Obuna", url="https://t.me/Ahmadjon_Abdulfotiyev")],
    [InlineKeyboardButton(text="Obuna", url="https://t.me/Rasmlar_va_malumotlar_uz")],
    [InlineKeyboardButton(text="Obuna", url="https://t.me/mobilegrafikan1")],
    [InlineKeyboardButton(text="Tekshirish", callback_data="submit")]
])


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Salom,\nPastdagi kanallarga obuna bo'ling. 👇", reply_markup=check)


@dp.callback_query(F.data == "submit")
async def sub_callback(call: CallbackQuery, bot: Bot, message: Message):
    user_status1 = await bot.get_chat_member(chat_id=-1002122098350, user_id=call.from_user.id)
    user_status2 = await bot.get_chat_member(chat_id=-1002081019692, user_id=call.from_user.id)
    user_status3 = await bot.get_chat_member(chat_id=-1001222394434, user_id=call.from_user.id)
    await message.answer("Siz obuna bo'lsangizgina bu botdan foydalana olasiz!")
    if user_status1.status != "left" or user_status2.status != "left" or user_status3 != "left":
        await bot.send_message(call.from_user.id, "Tabriklayman, siz royxatdan o'ta olasiz.")
    else:
        await bot.send_message(call.from_user.id, "Uzur, siz obuna bo'lmagansiz", reply_markup=check)
        text = "Kanalga obuna bo'lmagansiz ⚠️"
        show_alert = True
        await call.answer(text, show_alert=show_alert)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
