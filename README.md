# Бот для прослушивания реле
### Технологии, используемые ботом

1) aiogram
2) управлние реле при помощи RPi.GPIO


### Как работает бот, что умеет?

- Бот может принять запрос пользователя через кнопку;
- Бот управляет состоянием реле, в зависимости от выбранного режима;
- Бот обрабатывать команду /start выдавая первоначальную guidelines-информацию;
- Бот может обрабатывать команду /help, для выдачи команд, для взаимодействия с ботом
- Бот асинхронно отслеживает состояние реле, отпарвляет в чат сообщение по истечению работы временного режима
