from twitterscraper import query_tweets
# UserAgent Is the user agent, also called the header, is a string of characters, equivalent to the browser ID number When crawling a website with a crawler, changing it frequently can avoid triggering ...
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

if __name__ == '__main__':
    list_of_tweets = query_tweets("Tesla", 10)

    # print the retrieved tweets to the screen:
    for tweet in list_of_tweets:
        print(tweet.text)
