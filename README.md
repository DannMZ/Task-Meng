# Django REST API з використанням Conda

Цей проект демонструє, як створити простий REST API на Django, використовуючи `conda` для керування середовищем.

## 📌 Вимоги

- Python 3.9+
- Conda (Miniconda або Anaconda)
- Django
- Django REST framework

## 🚀 Встановлення

### 1. Клонування репозиторію
```bash
git clone https://github.com/yourusername/myproject.git
cd myproject
```

### 2. Створення та активація середовища Conda
```bash
conda create --name mydjangoenv python=3.9
conda activate mydjangoenv
```

### 3. Встановлення залежностей
```bash
pip install django djangorestframework
```

### 4. Налаштування бази даних
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

## 🔥 Використання API

### Отримати список елементів
```bash
GET http://127.0.0.1:8000/api/items/
```

### Додати новий елемент
```bash
POST http://127.0.0.1:8000/api/items/
Content-Type: application/json

{
    "name": "Example Item",
    "description": "This is an example description."
}
```

## 🛠 Структура проекту
```
myproject/
│── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── myapp/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── manage.py
```
---

💡 **Автор**: Mazarin

