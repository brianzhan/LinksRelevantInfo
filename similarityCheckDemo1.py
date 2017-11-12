from paralleldots import set_api_key, get_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social
#DO NOT randomly test, limited to 100 calls/day, for testing go to: https://www.paralleldots.com/semantic-analysis
# more API examples here: https://github.com/ParallelDots/ParallelDots-Python-API

set_api_key("rjIdkelw0TpgqoMXvVm3GU6ZSmrlIQCawicY5mGyB0I")

test = similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" )
print(test)