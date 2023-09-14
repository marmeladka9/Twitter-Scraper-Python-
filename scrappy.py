from tweety import Twitter
import pandas as pd

# Initialize the Twitter app
app = Twitter("session")
app.sign_in('Vladislava6792', 'nvaltaas30061980')

# Search for tweets
tweets = app.search('Apple', 50)

# Create an empty list to store tweet data
tweet_data = []

# Loop through tweets to gather data
for tweet in tweets:
    # Convert datetime to a timezone-unaware object
    created_on_naive = tweet.created_on.replace(tzinfo=None)
    date_naive = tweet.date.replace(tzinfo=None)

    tweet_data.append({
        'ID': tweet.id,
        'Created On': created_on_naive,
        'Date': date_naive,
        'Author': tweet.author,
        'Is Retweet': tweet.is_retweet,
        'Retweeted Tweet': tweet.retweeted_tweet,
        'Is Quoted': tweet.is_quoted,
        'Quoted Tweet': tweet.quoted_tweet,
        'Is reply': tweet.is_reply,
        'Is sensitive': tweet.is_sensitive,
        'Reply counts': tweet.reply_counts,
        'Quote counts': tweet.quote_counts,
        'Replied to': tweet.replied_to,
        'Bookmark count': tweet.bookmark_count,
        'Views': tweet.views,
        'Likes': tweet.likes,
        'Language': tweet.language,
        'Place': tweet.place,
        'Soruce': tweet.source,
        'Audio space id': tweet.audio_space_id,
        'Media': tweet.media,
        'User Mentions': tweet.user_mentions,
        'URLS': tweet.urls,
        'Hashtags': tweet.hashtags,
        'Symbols': tweet.symbols,
        'Community note': tweet.community_note,
        'Url of tweet': tweet.url,
        'Threads': tweet.threads,
        'Comments': tweet.comments,
    })

    #что можно сделать с твитом(его методы)
    # tweet.get_comments(pages) - даёт список коментариев
    # tweet.iter_comments(pages) - даёт ответы на этот твит
    # tweet.like() - лайкает твит
    # tweet.retweet() - ретвит
    # tweet.get_reply_to() - получает твит на который отвечает этот твит
# Create a DataFrame from the tweet data
df = pd.DataFrame(tweet_data)

# Save DataFrame to Excel
df.to_excel('tweets.xlsx', index=False, engine='openpyxl')
