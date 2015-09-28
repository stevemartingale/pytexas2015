import json
import os
import sys
from time import sleep
from flask import Flask, request
from kafka import SimpleProducer, KafkaClient


TOPIC_NAME = "sensor_temp"

try:
    KAFKA_IP = os.environ['KAFKA_PORT_9092_TCP_ADDR']
    KAFKA_PORT = os.environ['KAFKA_PORT_9092_TCP_PORT']
except KeyError:
    print "Please set the environment variables for KAFKA"
    sys.exit(1)


application = Flask(__name__)
sleep(10)  # hack to wait for kafka to be up in docker deloyment
kafka = KafkaClient("{0}:{1}".format(KAFKA_IP, KAFKA_PORT))
producer = SimpleProducer(kafka)


@application.route('/')
def home():
    return "<h1>Hello World</h1>"


@application.route('/temperature', methods=['POST'])
def temperature():
    producer.send_messages(TOPIC_NAME, json.dumps(request.json))
    return "ok"


kafka.ensure_topic_exists(TOPIC_NAME)
if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
