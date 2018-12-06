import datetime
import time
import requests

from gpiozero import Button


input = Button(2)
_HOUR = 3600000



def send_post(val):
    endpoint = "http://3.17.91.69/set_value"
    value = str(val)
    data = {'value':value}
    r = requests.post(url = endpoint, data = data)

def save_counting(valor):
    with open('count/counter.dat', 'w') as file
     file.write(valor)

def open_count():
    with open('count/counter.dat', 'r') as file
    return file.read().replace('\n', '')

# Setup
counter = open_count
start_time = time.time()
    # elapsed_time = time.time() - start_time

while True:

    if input.when_pressed :
        counter = counter + 1

    elapsed_time = time.time() - start_time

    if elapsed_time > _HOUR:
        save_counting(counter)
        send_post(counter)
        start_time = time.time()
