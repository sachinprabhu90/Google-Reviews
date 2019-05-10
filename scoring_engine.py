import nltk
import pandas as pd
import csv
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datetime

'''
created date: 08-Apr-2019
Last Edited date: 06-May-2019
In case of queries: sachin.prabhu@ril.com

Intended to score individual user reviews a score between -1 to +1 using nltk.
the scores file is in path_out.
'''




def score_reviews(df_in,path_out):
    '''
    returns input file with score column at path_out
    '''
    #df_in=pd.read_csv('D:\\review.csv') #for testing
    comments = list(df_in["text"]) #select the column with reviews
    sia = SentimentIntensityAnalyzer() #init analyzer

    #adding the column for scores
    scores=[]


    for sentence in comments:
        try:
            ss = sia.polarity_scores(sentence)
            scores.append(ss['compound']) #compound score
        except AttributeError: #in case if the review is of unsupported type
            scores.append(0)

    df_out= df_in #copying the in_df
    df_out['scores']=scores

    #cleaning the data
    df_in['post_date']=pd.to_datetime(df_in['time'], unit='s').dt.date
    df_in['post_time']=pd.to_datetime(df_in['time'], unit='s').dt.time
    df_in.to_csv(path_out,index=False)
    df_in=pd.read_csv(path_out)
    #df_in = df_in.drop({'time','Unnamed: 0'},axis=1) #workaround and needs to be changed

    # below code block checks if the file exists
    # if True, appends df_out and writes to csv
    # if not, writes to csv directly
    df_in.to_csv(path_out,index=False)
