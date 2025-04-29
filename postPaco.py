import requests, humedad

valorHumedad = humedad.getHumedad()
url = 'http://raspberrypi.local:60221/humidity'
myobj = {
    "id": "aaaa1111",
    "value": valorHumedad
}

x = requests.post(url, json = myobj)

print(x.text)