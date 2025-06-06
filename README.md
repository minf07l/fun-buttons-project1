# Number Storage Web App

Простое веб-приложение для сохранения и отображения чисел. Состоит из двух страниц:
- **Страница сохранения**: ввод числа и сохранение в локальное хранилище браузера
- **Страница показа**: отображение последнего сохраненного числа

## 🏗️ Технологический стек

- **Frontend**: React + React Router + CSS
- **Хранилище**: localStorage (браузер)
- **Развертывание**: GitHub Pages

## 🚀 Быстрый старт

### Для GitHub Pages (рекомендуется)

1. **Форк репозитория** или создайте новый с этим кодом
2. **Настройте GitHub Pages**:
   - Перейдите в Settings → Pages
   - Source: Deploy from a branch
   - Branch: main → /docs (или настройте GitHub Actions)
3. **Сайт будет доступен по адресу**: `https://yourusername.github.io/repository-name`

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd number-storage-app
```

2. Установите зависимости:
```bash
cd frontend
npm install
```

3. Запустите приложение:
```bash
npm start
```

4. Откройте в браузере: http://localhost:3000

### Сборка для продакшена

```bash
npm run build
```

Статические файлы будут созданы в папке `build/`.

## 📁 Структура проекта

```
number-storage-app/
├── frontend/
│   ├── src/
│   │   ├── App.js        # Основной компонент React
│   │   ├── App.css       # Стили
│   │   └── index.js      # Точка входа
│   ├── package.json      # Node.js зависимости
│   └── public/           # Статические файлы
├── docs/                 # Сборка для GitHub Pages
└── README.md            # Этот файл
```

## 🖥️ Использование приложения

1. **Главная страница** (Сохранение):
   - Введите любое число в поле ввода
   - Нажмите кнопку "Save"
   - Число сохранится в localStorage браузера

2. **Страница показа** (/show):
   - Нажмите кнопку "Show"
   - Увидите последнее сохраненное число
   - Если число не сохранено, увидите "none"

3. **Навигация**:
   - Используйте ссылки для перехода между страницами

## 🌐 Развертывание на GitHub Pages

### Вариант 1: Ручная сборка

1. Соберите проект:
```bash
cd frontend
npm run build
```

2. Скопируйте содержимое `build/` в папку `docs/`
3. Закоммитьте и запуште изменения
4. Настройте GitHub Pages на папку `docs/`

### Вариант 2: GitHub Actions (автоматически)

Создайте файл `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
        
    - name: Install dependencies
      run: |
        cd frontend
        npm install
        
    - name: Build
      run: |
        cd frontend
        npm run build
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./frontend/build
```

## ✨ Особенности

- **Без backend**: Работает полностью в браузере
- **Быстрая загрузка**: Статические файлы
- **Адаптивный дизайн**: Работает на всех устройствах
- **Анимации**: Красивые переходы и эффекты
- **Локальное хранение**: Данные сохраняются между сессиями

## 🔧 Настройка для GitHub Pages

### Важные моменты:

1. **BrowserRouter**: Для GitHub Pages нужно использовать `HashRouter` или настроить 404.html
2. **Public URL**: Убедитесь, что пути корректны для поддиректории
3. **HTTPS**: GitHub Pages автоматически использует HTTPS

### Альтернативная настройка для поддиректорий:

В `package.json` добавьте:
```json
{
  "homepage": "https://yourusername.github.io/repository-name",
}
```

## 🛠️ Разработка

### Добавление новых функций
1. **Новые страницы**: Добавьте Route в App.js
2. **Стили**: Измените App.css
3. **Логика**: Добавьте функции в компоненты

### Локальное хранилище
- **Ключ**: `savedNumber`
- **Формат**: Строка с числом
- **API**: `localStorage.getItem()` и `localStorage.setItem()`

## 📱 Совместимость

- ✅ Chrome, Firefox, Safari, Edge
- ✅ iOS Safari, Android Chrome
- ✅ Десктоп и мобильные устройства

## 📝 Лицензия

MIT License

## 🤝 Вклад в проект

1. Сделайте форк репозитория
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request