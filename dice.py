import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message

bot = Bot("")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}")




@dp.message(Command("play"))
async def play_games(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    await message.answer(f"{x.dice.value}")


@dp.message()
async def echo(message: Message):
    await message.answer(f"I don't underestand u!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())