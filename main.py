import requests
import os
import telegram
import random
from dotenv import load_dotenv


def download_comic(num_comics):
    url = f'https://xkcd.com/{num_comics}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()
    comics_url = response.json()['img']
    comics_alt = response.json()['alt']

    download_image = requests.get(comics_url)
    download_image.raise_for_status()

    comic_content = download_image.content

    with open('Files/comics.png', 'wb') as file:
        file.write(comic_content)

    return comics_alt


def search_all_comics():
    url = 'https://xkcd.com/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    last_comics = response.json()['num']
    num_comics = random.randint(1, last_comics)

    return num_comics


def publish_photo(bot, chat_id, alt_text):
    with open('Files/comics.png', 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file, caption=alt_text)


if __name__ == "__main__":
    load_dotenv()
    os.makedirs('Files', exist_ok=True)

    telegram_token_api = os.getenv("TG_TOKEN_API")
    telegram_chat_id = os.getenv("TG_CHAT_ID")

    bot = telegram.Bot(token=telegram_token_api)

    num_comics = search_all_comics()

    alt_text = download_comic(num_comics)

    publish_photo(bot, telegram_chat_id, alt_text)

    os.remove("Files/comics.png")
