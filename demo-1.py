#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.client import Telegram

tg = Telegram(
    api_id='23784791',
    api_hash='fbdf07ff5007992b897788979678f65a',
    phone='+639995249778',
    database_encryption_key='123456',
)

tg.login()

# this function will be called
# for each received message


def new_message_handler(update):
    print('New message!')


tg.add_message_handler(new_message_handler)
tg.idle()  # blocking waiting for CTRL+C
