# test-kanalservis
Приложение на python, Django.
Данные берутся из таблицы https://docs.google.com/spreadsheets/d/1OXm9Wx-9SESzA2bWXo51Tt5p03CvReIbaMwbahKHFVo/edit?usp=sharing
Данные записываются в бд на postgresql, при этом добавляется колонка со стоимостью в российских рублях. 
Актуальный курс доллара на текущую дату получается с сайта цб рф: http://www.cbr.ru/development/sxml/
Приложение имеет 2 урл:
Один - для того, чтобы обновлялись данные в бд, когда в таблице редактируются какие-либо значения
Второй - для просмотра данных на сайте.
Тестовое задание:
Необходимо разработать скрипт на языке Python 3, который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться)
Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:
4. a. Упаковка решения в docker контейнер
    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.
5. Решение на проверку передается в виде ссылки на проект на Github.
В описании необходимо указать ссылку на ваш Google Sheets документ (открыть права чтения и записи для пользователя amkolotov@gmail.com), а также инструкцию по запуску разработанных скриптов.
