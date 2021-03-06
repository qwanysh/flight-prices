# flight-prices

```
git clone git@github.com:qwanysh/flight-prices.git
cd flight-prices
docker-compose up -d

# Открыть браузер по адресу localhost:8000/flights, там постепенно будут появляться направления со значениями дешевых цен
```

#### Технологии:
- FastAPI (асинхронный фреймворк)
- Peewee (ORM)
- Celery (фоновые задачи)
- Redis (брокер сообщений)
- Uvicorn (ASGI сервер)
- SQLite (база данных)

#### Как это работает:
- При запуске приложения делаются асинхронные запросы на рейсы по направлениям
- Создаются периодичные celery-task на проверку рейсов, при успешной проверке рейс сохраняется в базу данных
- В API отображаются рейсы за последние 24 часа, сгруппированные по направлениям, с минимальной ценой на направление

#### Что не успел реализовать:
- Каждодневное обновление в 00:00 (нужно поставить `FlightsChecker(config.ROUTES_LIST).run()` в celery-periodic-task)
- Логирование
- Обработка ошибок при проверочных запросах
