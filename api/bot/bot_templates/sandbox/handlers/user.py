from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    await msg.reply("Hello")


@router.message()
async def message(msg: Message):
    await msg.reply(msg.text)