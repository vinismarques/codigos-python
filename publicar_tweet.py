import oauth2
import urllib.parse


consumer_key = "8ohbLTBI2lkVJYIx9oxcilgVI"
consumer_secret = "lLZiJBRAAftLmoR2to4dO2OoKrwHd98m8Dr5jdgKHZ4Cgb59oe"

token_key = "954110846090797056-E6K9J2RMMjivrWAiRIHWVbkEc8FXycl"
token_secret = "SckBt6vw37nTAzaRbYHZwqtZK85Bq9U81O5ODUTCk9Ltc"

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

query = input("Publicar: ")
query_codified = urllib.parse.quote(query)

request = client.request(
    f"https://api.twitter.com/1.1/statuses/update.json?status={query_codified}",
    method="POST",
)
print(request)
