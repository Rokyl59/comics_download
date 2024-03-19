import requests
import os
import telegram
import random
from dotenv import load_dotenv


def alt_text_comics(num_comics):
    url = f'https://xkcd.com/{num_comics}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()
    comics_alt = response.json()['alt']

    return comics_alt


def download_comics_image(num_comics):
    url = f'https://xkcd.com/{num_comics}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()
    comics_url = response.json()['img']

    download_image = requests.get(comics_url)
    download_image.raise_for_status()

    content_comics = download_image.content
    os.makedirs('Files', exist_ok=True)

    with open('Files/comics.png', 'wb') as file:
        file.write(content_comics)


def search_all_comics():
    url = 'https://xkcd.com/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    last_comics = response.json()['num']
    num_comics = random.randint(1, last_comics)

    return num_comics


def publish_photos(bot, chat_id, alt_text):
    with open('Files/comics.png', 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file, caption=alt_text)


if __name__ == "__main__":
    load_dotenv()
    telegram_token_api = '7100534990:AAG52xwXfncSxcDIbUTCTZTa3RpDOUF6C1k'
    telegram_chat_id = os.getenv("")

    bot = telegram.Bot(token=telegram_token_api)

    num_comics = search_all_comics()

    download_comics_image(num_comics)
    alt_text = alt_text_comics(num_comics)

    publish_photos(bot, telegram_chat_id, alt_text)

    os.remove("Files/comics.png")
