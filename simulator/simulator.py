from random import randint, normalvariate, random
from time import sleep
import requests


class Machine(object):
    def __init__(self, machine_id):
        self.id = machine_id
        self.mean = randint(10, 150)
        self.variance = randint(5, 60)
        self.throughput_factor = random()

    def get_temperature(self):
        return abs(int(normalvariate(self.mean, self.variance)))

    def finished_toy(self):
        if random() < self.throughput_factor:
            return True
        else:
            return False


def send_temp_message(machine_id, temp):
    message = {"machine_id": machine_id, "temperature": temp}
    return requests.post("http://127.0.0.1:5000/temperature", json=message)

machines = [Machine(x) for x in range(0, 8)]

while True:
    for machine in machines:
        if machine.finished_toy():
            temperature = machine.get_temperature()
            r = send_temp_message(machine.id, machine.get_temperature())
            print r.text
    sleep(2)
