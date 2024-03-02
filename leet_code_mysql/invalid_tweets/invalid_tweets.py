import pandas as pd

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype(
    {'tweet_id': 'Int64', 'content': 'object'})

# Using .apply(len)
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['content_length'] = tweets['content'].apply(len)
    filtered_tweets = tweets[tweets['content_length'] > 15]
    return filtered_tweets['tweet_id']

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets.content.apply(len) > 15][['tweet_id']]

# Using str.len()
def invalid_tweets(df: pd.DataFrame) -> pd.DataFrame:
    mask = df['content'].str.len() > 15
    return df.loc[mask][['tweet_id']]

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]


# Using dictionary and list
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    dict_ = dict(tweets.values)
    lis = list()
    for i in dict_.keys():
        if len(dict_[i]) > 15:
            lis.append(i)
    return pd.DataFrame(lis, columns = ["tweet_id"])