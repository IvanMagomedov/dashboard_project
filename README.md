
# 📊 Django Dashboard с графиками и фильтрацией

Этот проект — простой и наглядный дашборд на Django с графиками от Chart.js и таблицей, подключённой к базе данных. Отлично подойдёт как портфолио для демонстрации навыков работы с Django, динамическими данными, визуализацией и фильтрами.

---

## 🔧 Технологии

- **Backend:** Django
- **Frontend:** Chart.js, Django Templates
- **База данных:** SQLite
- **Прочее:** Bootstrap/Tailwind, фильтрация по дате, админ-панель

---

## 🖥 Возможности

- 📈 График продаж по дням
- 🗂 Таблица с данными
- 📅 Фильтрация по дате
- 🧮 Агрегация данных
- 🔐 Админка для управления

---

## 🚀 Как запустить

### 1. Клонируй репозиторий:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Создай виртуальное окружение и активируй:

python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate     # для Windows

3. Установи зависимости:

pip install -r requirements.txt

4. Примени миграции и создай суперпользователя:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. (Опционально) Загрузить тестовые данные:

python manage.py load_test_data

6. Запусти сервер:

python manage.py runserver

Перейди в браузер по адресу: http://127.0.0.1:8000

⸻

📁 Структура проекта

dashboard_project/
├── dashboard_app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── management/
│       └── commands/
│           └── load_test_data.py
├── dashboard_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── requirements.txt
└── README.md


⸻

🛠 План по доработке
	•	Фильтрация по продукту
	•	AJAX-фильтрация без перезагрузки страницы
	•	Загрузка CSV
	•	Авторизация и роли пользователей

⸻

🧑‍💻 Автор

@твое_имя — разработчик и автор проекта.
Если проект был полезен — оставь ⭐️ на GitHub!

⸻

📃 Лицензия

MIT License — используй, улучшай и не забывай указать автора 😊

