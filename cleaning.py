import json
import string
import pandas as pd
import joblib

def readjson():
    tweets_data=[]
    file=open("tweets.txt",'r')
    for line in file:
        try:
            t=json.loads(line)
            tweets_data.append(t['text'])
        except:
            #print("error")
            continue
    print(len(tweets_data))
    #print(tweets_data)
    df=pd.DataFrame()
    df['text']=tweets_data
    print(df)
    df.to_csv("readtweets.csv",encoding="utf8")
    #df['text']=map(lambda tweet:tweet['text'],tweets_data)
    #print(df.text)

def clean_tweets():
#reading csv file into panda dataframe
    df = pd.read_csv("kot.csv",sep=";", error_bad_lines=False)
    print("CSV file read")

    print("Removing RTs")
    df.text=df.text.str.replace("RT","",False)
    df.text=df.text.str.lower()#change tweets to lowercase

    print("Removing usernames from tweets")
    df.text=df.text.str.replace("@\w*\s?","")#remove usernames

#remove url links froms tweets
    print("Removing urls")
    df.text=df.text.str.replace("https?:\/\/.*[\r\n]*","")

#removing hashtags
    print("Removing hashtags")
    df.text=df.text.str.replace("#\w*","")#removing hashtags

#removing punctuations
    print("Removing punctuations")
    df.text=df.text.str.translate(str.maketrans("","",string.punctuation))

#remove non utf8 characters
    df.text=df.text.str.replace("[^\x00-\x7F]+","")

    print("Writing clean CSV")
    df.to_csv("clean_tweets.csv",encoding="utf8")

def predict():
    df=pd.read_csv("clean_tweets.csv")
    df=df.dropna(how='any')
    df=df.drop_duplicates()
    model=joblib.load("pickle_model.pkl")
    df['label']=model.predict(df.text)
    print(df.label)
    df.to_csv("predicted.csv",encoding="utf8")
    #print(model.predict(df.text))
    print("read")

def main():
    readjson()
    clean_tweets()
    predict()

if __name__=="__main__":
        main()
