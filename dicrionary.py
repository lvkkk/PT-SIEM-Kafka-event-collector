#!/usr/bin/env python

# Справочник, требует установки на агенте библиотеки python-kafka
from kafka import KafkaConsumer
from datetime import datetime
import json

def collect(target, settings, savepoint):
    consumer = KafkaConsumer(bootstrap_servers=settings['server'],
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000,
                             enable_auto_commit=True,
                             auto_commit_interval_ms=1000,
                             group_id=settings['group_id'])
    consumer.subscribe([settings['topic']])
    iter = 0
    for message in consumer:
        msgtime = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        msgtext = message.value.decode("utf-8")
        if iter >= 1000: # количество записей считываемых за один цикл работы скрипта
            break
        else:
            iter = iter + 1
        yield json.dumps(   {"action": "info",
                            "object": "Kafka_stream",
                            "status": "ongoing",
                            "event_src.category": "Other", 
                            "event_src.title": "event-title", 
                            "event_src.vendor": "event-vendor", 
                            "importance": "info", 
                            "msgid": str(message.offset),
                            "time": msgtime, 
                            "body": msgtext
                            }
                        )
    yield False
    yield savepoint

if __name__ == "__main__":
    col = collect(1,{"server":'kafkaserver_IP:PORT', "group_id":'GROUPID', "topic":'TOPIC_NAME'},3) 
    for it in col:
        print(it)
