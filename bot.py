import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv("bot_token")

if bot_token is None :
    print("Токен не задан или не найден файл .env")
    exit()

bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    main_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text = "Обо мне 🚧 В разработке", callback_data = "in_dev")],
            [InlineKeyboardButton(text="Мои соцсети 🚧 В разработке", callback_data="in_dev")],
            [InlineKeyboardButton(text="Заказать бота 🚧 В разработке", callback_data="in_dev")],
            [InlineKeyboardButton(text="Связаться со мной🚧 В разработке", callback_data="in_dev")]
        ]
    )
    await message.answer("""Привет! Если вы читаете это сообщение,
    значит вы планируете нанять меня на работу,
    заказать разработку tg-бота
    или каким-то образом случайно нашли этого бота в интернете.
    В любом случае, я рад приветствовать вас в моём боте-визитке.
    Вы можете ознакомиться с функционалом бота, используя кнопки ниже.""",
                         reply_markup=main_keyboard)
    print(message.model_dump_json(indent=4))


@dp.callback_query(F.data == "in_dev")
async def in_dev_click(callback: types.CallbackQuery):
    await callback.answer(
        text="Эта фича появится чуть позже! Бот находится в разработке.",
        show_alert=True
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())