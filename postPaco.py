import requests, humedad2 as humedad

valorHumedad = humedad.getHumedad(0)
url = 'http://raspberrypi.local:60221/humidity'
myobj = {
    "id": "aaaa1111",
    "value": valorHumedad
}

x = requests.post(url, json = myobj)

valorHumedad = humedad.getHumedad(1)
myobj = {
    "id": "aaaa2222",
    "value": valorHumedad
}

x = requests.post(url, json = myobj)