# PT-SIEM-Kafka-event-collector
**Описание**

Проект содержит скрипт получения событий из потоков Kafka и пример настроек профиля MP SIEM.
Скрипт базируется на библиотеке [kafka-python](https://github.com/dpkp/kafka-python) и требует её наличия на агентах. Для установки kafka-python необходимо поместить в архив `C:\Program Files (x86)\Positive Technologies\MaxPatrol SIEM Agent\modules\PyEventCollector\CustomEventCollector.zip` папку kafka:

![kafkadir](/kafkadir.png)

**Установка и настройка**

Создать справочник MP SIEM и скопировать в него содержимое скирпта [dicrionary.py](/dicrionary.py).

Создать на базе профиля Custom Event Collector новый профиль, указать в его настройках необходимость обращения к созданному справочнику и параметры подключения к Kafka.
Настройки подключения задаются в формате JSON и имеют вид:

`{
    "server": "kafkaserver_IP:PORT",
    "group_id": "GROUPID",
    "topic": "TOPIC_NAME"
 }`

, где
- GROUPID - имя группы kafka
- TOPIC_NAME - название топика kafka из которого предполагается считывать записи
- kafkaserver_IP:PORT - адрес и порт сервера kafka


Пример настроек:

`{
    "server": "1.1.1.1:9092",
    "group_id": "ptsiem_gp",
    "topic": "security_events"
}`

Полный JSON файл настроек профиля для однократной работы задачи в файле [profile.js](/profile.js)
