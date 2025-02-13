# Task Manager API

Task Manager API - це веб-додаток для управління завданнями, створений на основі Django REST Framework (DRF) з використанням SQLite та Conda.

## 🚀 Функціональність
- Створення, редагування та видалення завдань
- Перегляд списку завдань
- API для взаємодії з завданнями (CRUD)
- Використання Django REST Framework

## 🛠️ Встановлення та запуск
### 1. Клонування репозиторію
```bash
git clone https://github.com/DannMZ/Task-Meng
cd task-manager
```

### 2. Створення та активація віртуального середовища (Conda)
```bash
conda create --name taskmanager python=3.10 -y
conda activate taskmanager
```

### 3. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 4. Виконання міграцій
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

Сервер буде доступний за адресою: `http://127.0.0.1:8000/`

## 📡 API Роутинг
| Метод | URL | Опис |
|--------|----------------------|---------------------------|
| GET | `/api/tasks/` | Отримати список завдань |
| POST | `/api/tasks/` | Створити нове завдання |
| GET | `/api/tasks/{id}/` | Отримати конкретне завдання |
| PUT | `/api/tasks/{id}/` | Оновити завдання |
| DELETE | `/api/tasks/{id}/` | Видалити завдання |

## 📂 Структура проекту
```
task_manager/
│── tasks/
│   ├── migrations/
│   ├── templates/tasks/
│   │   ├── task_list.html
│   │   ├── task_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── task_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── db.sqlite3
│── manage.py
│── requirements.txt
│── README.md
```

## 📝 Ліцензія
Цей проект розповсюджується під ліцензією MIT. Вільно використовуйте його та розвивайте!

---

🔧 Автор: **Mazarin**  
📧 Контакти: [gnatuksapovaldaniil@gmail.com](mailto:gnatuksapovaldaniil@gmail.com)  