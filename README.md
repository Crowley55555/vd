# КиберКоролевство - Цифровое государство будущего

![КиберКоролевство](static/image/logo.png)

Веб-приложение на Flask, представляющее виртуальное цифровое государство с современным дизайном и интерактивными элементами.

## 🚀 Особенности

- 🌌 Футуристический неоновый дизайн
- 🗺️ Интеграция с Яндекс.Картами
- ⏰ Отображение времени в часовом поясе пользователя
- 📱 Полностью адаптивный интерфейс
- 📝 Формы обратной связи с анимацией
- 📱 Мобильное меню с "бургером"

## 🛠 Технологии

- **Backend**: Python 3.10+, Flask
- **Frontend**: Bootstrap 5.3, JavaScript
- **Карты**: API Яндекс.Карт
- **Иконки**: Bootstrap Icons

## ⚙️ Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/ваш-username/киберкоролевство.git
cd киберкоролевство
Создать и активировать виртуальное окружение:

bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
Установить зависимости:

bash
pip install -r requirements.txt
Создать файл .env и добавить API ключ:

ini
YANDEX_MAPS_API_KEY=ваш_ключ
FLASK_SECRET_KEY=ваш_секретный_ключ
Запустить приложение:

bash
flask run
🌐 Структура проекта
/киберкоролевство
├── /static
│   ├── /css
│   ├── /js
│   └── /image
├── /templates
│   ├── index.html
│   ├── blog.html
│   └── contacts.html
├── main.py
├── requirements.txt
└── README.md
📌 Маршруты
/ - Главная страница

/blog/ - Блог технологий будущего

/contacts/ - Контакты и карта

📜 Лицензия
MIT License. См. файл LICENSE.