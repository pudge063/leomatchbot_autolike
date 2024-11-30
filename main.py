from telethon import TelegramClient, events
import os
import sys
import asyncio
from config import api_id, api_hash, phone_number, SAVE_PATH
from checker import Checker

client = TelegramClient("session_name", api_id, api_hash)
checker = Checker()

last_message = None


@client.on(events.NewMessage(from_users="leomatchbot"))
async def message_handler(event):
    global last_message
    last_message = event.text
    print(f"Получено сообщение: {last_message}")


async def send_likes(like_count):
    await client.start()

    await client.send_message("leomatchbot", "1")

    for _ in range(like_count):
        print("Ожидание нового сообщения...")
        while last_message is None:
            await asyncio.sleep(1)

        is_exists = checker.check_in_list(last_message)

        if is_exists is False:
            await client.send_message("leomatchbot", "1")
            print("Лайк отправлен.")
        else:
            await client.send_message("leomatchbot", "3")
            print("Скип анкеты.")

        await asyncio.sleep(1)


async def main():
    if len(sys.argv) > 1:
        try:
            like_count = int(sys.argv[1])
            await send_likes(like_count)
        except ValueError:
            print("Ошибка: аргумент должен быть числом.")
    else:
        print("Ошибка: не указан аргумент для количества лайков.")


if __name__ == "__main__":
    asyncio.run(main())
