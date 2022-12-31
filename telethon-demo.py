
from telethon import TelegramClient
import schedule
import time

api_id = 23784791
api_hash = 'fbdf07ff5007992b897788979678f65a'
client = TelegramClient('anon', api_id, api_hash)


async def main():
    me = await client.get_me()
    # print(me.stringify())

    while True:
        message = await client.send_file(
            -862023086, './Woz.png',
            caption='妮妮小店菜单，欢迎下单品尝！',
            title='It is title!',
        )
        # print(message.raw_text)
        time.sleep(3600)

with client:
    client.loop.run_until_complete(main())
