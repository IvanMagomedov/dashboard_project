# 📊 Django Dashboard с графиками и фильтрацией

Проект представляет собой интерактивный дашборд на Django с графиками на Chart.js, отображающий динамику продаж по дням. Подходит для портфолио — демонстрирует работу с базой данных, визуализацией и фильтрацией данных.

---

## 🔧 Технологии

- **Backend:** Django 4+
- **Frontend:** Chart.js, HTML (Django Templates)
- **База данных:** SQLite (по умолчанию)
- **Дополнительно:** Bootstrap (или Tailwind), фильтрация по дате, таблица с данными

---

## 🖼 Скриншот

<img src="preview.png" width="800">

---

## 🚀 Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/твоя-ссылка/dashboard_project.git
   cd dashboard_project

	2.	Создай виртуальное окружение и активируй его:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


	3.	Установи зависимости:

pip install -r requirements.txt


	4.	Примените миграции и создайте суперпользователя:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


	5.	(Опционально) Загрузите тестовые данные:

python manage.py load_test_data


	6.	Запусти сервер:

python manage.py runserver



Открой http://127.0.0.1:8000

⸻

⚙️ Возможности
	•	📅 Фильтрация по дате
	•	📈 Динамический график (Chart.js)
	•	🗂 Таблица данных
	•	🧮 Агрегация сумм по дням
	•	🔐 Админ-панель

⸻

📁 Структура проекта

dashboard_project/
├── dashboard_app/
│   ├── models.py          # Модель SalesRecord
│   ├── views.py           # Отображение дашборда
│   ├── templates/         # Шаблон с графиком и таблицей
│   └── management/
│       └── commands/
│           └── load_test_data.py  # Команда генерации тестов
├── dashboard_project/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── requirements.txt
├── README.md


⸻

📌 Пример модели

class SalesRecord(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=100)
    amount = models.FloatField()


⸻

✅ Планы на улучшение
	•	Фильтрация по продукту
	•	Экспорт данных в CSV
	•	AJAX-загрузка без перезагрузки страницы
	•	Авторизация и роли

⸻

