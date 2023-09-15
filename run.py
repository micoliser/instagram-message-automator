#!/usr/bin/env python3
""" runs the message automator """
from automator.message_automator import MessageAutomator
from os import environ
from datetime import datetime, timedelta
import random
import schedule
import time


def send():
    """ runs the message automator """

    username = environ.get('INSTAGRAM_USERNAME')
    password = environ.get('INSTAGRAM_PASSWORD')

    messages = [
        'Remember to drink water. :)',
        'How many sachets of water have you drank today?.. Go and drink water.',
        'Drink water.',
        'Drink water, please. :)',
        'Water is good for you. Drink it.',
        'Leave what you are doing and drink water.',
        'Drink water Candy',
        'My baby, drink water.',
        'Drink water, my love.',
        'Oya, drink water.',
        'Fa slap you now, you will drink water.',
        'Don\'t let me come there and force you to drink water.',
        'I will press your neck if you don\'t goan drink water now'
    ]

    message_automator = MessageAutomator(username, password)
    try:
        message_automator.login()
    except Exception:
        pass
    message_automator.send_message('dept_of_european_lang_unilag_', random.choice(messages))
    # message_automator.close()

current_hour = datetime.now().hour
if current_hour < 8:
    initial_delay = (8 - current_hour) * 3600  # Seconds until 8 AM
else:
    initial_delay = (current_hour + 2 - 8) * 3600  # Seconds until next even hour after 8 AM

# Schedule the task to run every 2 hours
schedule.every().day.at("07:00").do(send)
schedule.every().day.at("09:00").do(send)
schedule.every().day.at("11:00").do(send)
schedule.every().day.at("13:00").do(send)
schedule.every().day.at("15:00").do(send)
schedule.every().day.at("17:00").do(send)
schedule.every().day.at("19:00").do(send)
schedule.every().day.at("21:00").do(send)
schedule.every().day.at("23:00").do(send)


if __name__ == "__main__":
    # Start the scheduling loop
    #while True:
        #schedule.run_pending()
        #time.sleep(1)
    send()
