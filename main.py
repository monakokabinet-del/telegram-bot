from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routers import router

load_dotenv()
TOKEN = "8523716699:AAFsMBDsabLu6Y2i84BiSkdYov0S4tAVrR4"

dp = Dispatcher()
dp.include_router(router)


async def main():
    bot = Bot(token=TOKEN)

    print("Start...")
    await dp.start_polling(bot)



if __name__== "__main__":
    asyncio.run(main())
