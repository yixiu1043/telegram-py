
from telethon import TelegramClient
import schedule
import time

# Remember to use your own values from my.telegram.org!
api_id = 23784791
api_hash = 'fbdf07ff5007992b897788979678f65a'
client = TelegramClient('anon', api_id, api_hash)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    async def job():
        client.send_file(
            -862023086, './Woz.png',
            caption='It is caption!',
            title='It is title!',
        )

        # Sending a message returns the sent message object, which you can use
        # print(message.raw_text)

    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(1)

with client:
    client.loop.run_until_complete(main())
