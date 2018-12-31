import oauth2
import json
import urllib.parse
# import pprint


consumer_key = "8ohbLTBI2lkVJYIx9oxcilgVI"
consumer_secret = "lLZiJBRAAftLmoR2to4dO2OoKrwHd98m8Dr5jdgKHZ4Cgb59oe"

token_key = "954110846090797056-E6K9J2RMMjivrWAiRIHWVbkEc8FXycl"
token_secret = "SckBt6vw37nTAzaRbYHZwqtZK85Bq9U81O5ODUTCk9Ltc"

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

query = input("Pesquisar por: ")
query_codified = urllib.parse.quote(query)

request = client.request(
    f"https://api.twitter.com/1.1/search/tweets.json?q={query_codified}&result_type=popular&lang=pt"
)
decodify = request[1].decode()
result_json = json.loads(decodify)
tweets = result_json["statuses"]

for tweet in tweets:
    print(tweet["user"]["screen_name"])
    print(tweet["text"])
    print()
