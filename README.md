# Twitter-Scraper-Python-
Tweety is a Python library, which means you need to download and install Python from https://www.python.org/downloads/ if you haven’t already. Once you have Python installed, upgrade pip and run:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade tweety-ns
```
# Signing In
The Twitter requires user to logged-in, in order to get any information. 
Before Singing In , please make sure you already have account on Twitter.
Most of the time , start is the only method you will interact with to login and create a session This Method will ask for Username, Password or any other information or action required for completing the log-in process.
```
from tweety import Twitter

app = Twitter("session")
app.sign_in(username, password)
print(app.user)
```
* By running this code 
* The Tweety will login to Twitter using the username and password provided 
* If the request was successful , the authentication cookies obtained from response will be saved in session.tw_session (filename is subject to the name of session) file.

# Search Filters
You can filter the Search function using these methods.

# Filter Latest Tweets
```
from tweety.filters import SearchFilters

# Assuming `app` is Twitter Client Object

app.search("#pakistan", filter_=SearchFilters.Latest())
from tweet in tweets:
    print(tweet)
```

# Filter Only Media Tweets
```
from tweety.filters import SearchFilters

# Assuming `app` is Twitter Client Object

app.search("#pakistan", filter_=SearchFilters.Media())
from tweet in tweets:
    print(tweet.media)
```

# Filter Only Users
```
from tweety.filters import SearchFilters

# Assuming `app` is Twitter Client Object

app.search("#pakistan", filter_=SearchFilters.Users())
from user in users:
    print(user)
```

# Tweet Audience Filter
You can filter the created Tweet Comment Audience function using these methods
```
from tweety.filters import TweetConversationFilters

# Assuming `app` is Twitter Client Object

app.create_tweet("Hi", filter_=TweetConversationFilters.PeopleYouMention())
```
# Filter Only People You Follow
```
from tweety.filters import TweetConversationFilters

# Assuming `app` is Twitter Client Object

app.create_tweet("Hi", filter_=TweetConversationFilters.PeopleYouFollow())
```
