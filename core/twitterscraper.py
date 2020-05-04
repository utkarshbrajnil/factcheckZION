

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

ipstr="covid-19"

begin_date = dt.date(2020,5,1)
end_date = dt.date(2020,5,4)

limit = 100
lang = "english"

tweets = query_tweets(ipstr,begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
df = pd.DataFrame(t.__dict__ for t in tweets)


