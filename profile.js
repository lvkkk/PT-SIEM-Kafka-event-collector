### Настройки профиля MP SIEM в формте json, где
#DICT_NAME - название справочника в который сохранен скрипт
#GROUPID - имя группы kafka
#TOPIC_NAME - название топика kafka из которого предполагается считывать записи
#kafkaserver_IP:PORT - адрес и порт сервера kafka


{
    "code": "@{DICT_NAME}",
    "event_type": "JSON",
    "settings": {
        "server": "kafkaserver_IP:PORT",
        "group_id": "GROUPID",
        "topic": "TOPIC_NAME"
    },
    "mode": "ONLY_OLD",
    "check_new_data_delay": 30
}
