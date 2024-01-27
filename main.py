import asyncio
import sys
from typing import Final
from telegram import Bot, Update

TOKEN: Final = '6812350682:AAGEa2DZdNczIldf0orRZjA2Afv6mysLk6o'

async def send_photo(photo_path, chat_id, bot, caption=None):
    with open(photo_path, 'rb') as photo_file:
        bot.send_photo(chat_id=chat_id, photo=photo_file, caption=caption)

async def send_photos_to_chat():
    # Replace these paths with the actual paths to your local photo files
    photo_paths = [
        'trends_1.png',
        'trends_2.png',
        'data\\08_reporting\\consecutive_Visits_plot.png',
    ]

    chat_id = '-4179541564'  # Replace with the actual chat ID where you want to send the photos

    captions = [
        "Hello! These are the latest blood donation trend plots for Borneo,Central & Central Region.",
        "Hello! These are the latest blood donation trend plots for Pusat Darah negara ,Southern & Northern Region .",
        "Hello! These are the stats for Donor's Retention."
    ]

    bot = Bot(token=TOKEN)

    # Send each photo with its corresponding caption concurrently
    await asyncio.gather(*(send_photo(photo_path, chat_id, bot, caption) for photo_path, caption in zip(photo_paths, captions)))

    # Stop the script after sending photos successfully
    sys.exit()

if __name__ == '__main__':
    # Send photos immediately when the script is run
    asyncio.run(send_photos_to_chat())
