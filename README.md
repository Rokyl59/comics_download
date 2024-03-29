# Загрузка и отправка комикса в телеграм


Этот скрипт на Python скачивает случайный комикс с XKCD и публикует его в указанный чат в Telegram. Он использует API XKCD для получения информации о комиксах и изображений, а также API бота Telegram для размещения этих комиксов в чате. Скрипт идеально подходит для ежедневной публикации дозы юмора для ваших друзей или сообщества.

## Предварительные требования

Перед запуском этого скрипта убедитесь, что у вас установлено следующее:

* Python версии 3.x
* Библиотека `requests`
* Библиотека `python-telegram-bot`
* Библиотека `python-dotenv`

Вы можете установить необходимые библиотеки с помощью requirements:

```python
pip install -r requirements.txt
```

## Настройка

1. Клонируйте репозиторий на ваш локальный компьютер.
```bash
git clone https://github.com/Rokyl59/comics_download.git
```

2. Создайте файл `.env` в корневом каталоге проекта. Этот файл должен содержать следующую переменную окружения:

* `TG_CHAT_ID`: ID чата в Telegram, в который вы хотите публиковать комиксы.

* `TG_API_TOKEN`: API бота, получить от _BotFather_

## Использование

Для запуска скрипта перейдите в каталог со скриптом и выполните:

```bash
python main.py
```

## Особенности

* Получает случайный комикс из XKCD.

* Загружает изображение комикса и сохраняет его локально.

* Публикует изображение комикса вместе с его альтернативным текстом (alt text) в указанный чат в Telegram.

* Очищает за собой, удаляя загруженное изображение после публикации.

# Важные замечания

* Убедитесь, что бот Telegram добавлен в чат, где вы намерены размещать комиксы.

* Скрипт создаст директорию Files для временного хранения загруженного комикса. Убедитесь, что ваша среда выполнения имеет необходимые разрешения.

* Этот скрипт использует жестко закодированную конфиденциальную информацию (токен API Telegram). В целях безопасности рекомендуется хранить такую информацию в переменных среды или использовать другие безопасные методы хранения.

 
