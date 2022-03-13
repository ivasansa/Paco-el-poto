import tweepy, config, humedad, datetime

# calling a client
client = tweepy.Client(
    consumer_key=config.keys['consumer_key'],
    consumer_secret=config.keys['consumer_secret'],
    access_token=config.keys['access_token'],
    access_token_secret=config.keys['access_token_secret']
)

valorHumedad = humedad.getHumedad()
while (valorHumedad > 100 or valorHumedad < 0):
    valorHumedad = humedad.getHumedad()


humedadPaco = str(valorHumedad)+"%"

response = client.create_tweet(text=humedadPaco)
print (datetime.datetime.now(),"-", response)