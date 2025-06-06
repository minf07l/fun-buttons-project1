# Number Storage Web App

Простое веб-приложение для сохранения и отображения чисел. Состоит из двух страниц:
- **Страница сохранения**: ввод числа и сохранение в базу данных
- **Страница показа**: отображение последнего сохраненного числа

## 🏗️ Технологический стек

- **Frontend**: React + React Router + Tailwind CSS
- **Backend**: FastAPI + Python
- **База данных**: MongoDB
- **Стили**: CSS + Tailwind

## 🚀 Быстрый старт

### Вариант 1: Docker (Рекомендуется)

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd number-storage-app
```

2. Запустите с помощью Docker Compose:
```bash
docker-compose up -d
```

3. Откройте в браузере: http://localhost:3000

### Вариант 2: Ручная установка

#### Предварительные требования
- Node.js (версия 16+)
- Python (версия 3.8+)
- MongoDB

#### Backend (FastAPI)

1. Перейдите в папку backend:
```bash
cd backend
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=number_storage
```

5. Запустите сервер:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

#### Frontend (React)

1. Перейдите в папку frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Создайте файл .env:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

4. Запустите приложение:
```bash
npm start
```

## 📁 Структура проекта

```
number-storage-app/
├── backend/
│   ├── server.py          # Основной файл FastAPI
│   ├── requirements.txt   # Python зависимости
│   └── .env              # Переменные окружения (создать вручную)
├── frontend/
│   ├── src/
│   │   ├── App.js        # Основной компонент React
│   │   ├── App.css       # Стили
│   │   └── index.js      # Точка входа
│   ├── package.json      # Node.js зависимости
│   └── .env              # Переменные окружения (создать вручную)
├── docker-compose.yml    # Docker конфигурация
└── README.md            # Этот файл
```

## 🔧 API Endpoints

- `GET /api/` - Проверка работы API
- `POST /api/save-number` - Сохранение числа
- `GET /api/get-number` - Получение последнего сохраненного числа

### Примеры использования API

Сохранить число:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"number": 42.5}' \
     http://localhost:8001/api/save-number
```

Получить число:
```bash
curl http://localhost:8001/api/get-number
```

## 🖥️ Использование приложения

1. Откройте главную страницу (Сохранение)
2. Введите любое число в поле ввода
3. Нажмите кнопку "Save"
4. Перейдите на страницу "Show" через навигационную ссылку
5. Нажмите кнопку "Show" для отображения сохраненного числа

## 🌐 Деплой

### Vercel (Frontend)
1. Подключите репозиторий к Vercel
2. Установите переменную окружения `REACT_APP_BACKEND_URL`
3. Деплой происходит автоматически

### Railway/Render (Backend)
1. Подключите репозиторий к платформе
2. Установите переменные окружения для MongoDB
3. Укажите команду запуска: `uvicorn server:app --host 0.0.0.0 --port $PORT`

### MongoDB Atlas (База данных)
1. Создайте бесплатный кластер на MongoDB Atlas
2. Получите строку подключения
3. Добавьте её в переменную окружения `MONGO_URL`

## 🛠️ Разработка

### Добавление новых функций
1. Backend: добавляйте новые endpoints в `server.py`
2. Frontend: создавайте новые компоненты в папке `src/`
3. Стили: используйте Tailwind CSS классы в `App.css`

### Тестирование
- Backend тесты: `python -m pytest`
- Frontend тесты: `npm test`

## 📝 Лицензия

MIT License

## 🤝 Вклад в проект

1. Сделайте форк репозитория
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request