import tweepy
import csv
consumer_key="gdIYUAOypp7dgFEMWz9wpuVC7"
consumer_secret="wqzYx4jHngjlaXMN4qTbR9Vn3szoBT2sukPuUjKuZpoAd0meHX"
access_token="806066029952729088-N1gWDFhxLGMgIIfBj47uUBJmeeMDNt6"
access_secret="hGqcm517Gl4g5NkVcOijWlXK0duMjtwAj0jf3hRYzLP2D"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('tweets.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)
def getkeywords():
    f=open("mycriteria.dat",'r')
    keywords=[]
    text=f.readline()
    text=text.split(';')
    for t in text:
        keywords.append

    return keywords;
    keywords = getkeywords()
    # print(keywords)

    csvWriter.writerow(["text"])
    print("here now")
    for tweet in tweepy.Cursor(api.search, q=keywords).items():
        print(tweet.text)
        csvWriter.writerow([tweet.text.encode('utf-8')])
