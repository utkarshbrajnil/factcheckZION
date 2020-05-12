import datetime as dt
import pandas as pd
from twitterscraper import query_tweets

#ipstr="covid-19"
def top_results(ipstr):
    two_months = dt.timedelta(days=60)
    end_date = dt.date.today()
    begin_date = end_date - two_months
    
    limit = 100
    lang = "english"
    
    tweets = query_tweets(ipstr, begindate=begin_date, enddate=end_date ,limit=limit, lang=lang)
    
    df = pd.DataFrame(t.__dict__ for t in tweets)
    df.sort_values(by=['likes','retweets','replies'], inplace=True, ascending=False)
    
    df.drop(df.columns[[2,3,5,6,8,11,13,17,18,19,20]], axis = 1, inplace = True)
    df = df[df.likes >=30]
    df.set_index('username',inplace=True)
    return (df)


def to_verify(df):
    screen_name_list= df["screen_name"].tolist()
    return (screen_name_list)

#ansdf = top_results("ivankatrump")
#verlist = to_verify(ansdf)
