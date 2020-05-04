import datetime as dt
import pandas as pd
from twitterscraper import query_tweets

ipstr="covid-19"

two_months = dt.timedelta(days=60)
end_date = dt.date.today()
begin_date = end_date - two_months

limit = 100
lang = "english"

tweets = query_tweets(ipstr, begindate=begin_date, enddate=end_date ,limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)


df.sort_values(by=['likes','retweets','replies'], inplace=True, ascending=False)
df.to_json(r'/home/aditya/factcheckZION/core/op/scrapesearch.json')

