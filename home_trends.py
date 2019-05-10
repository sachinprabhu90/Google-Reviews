from google_review import get_review
import pandas as pd
from scoring_engine import score_reviews #cleans df and processes natural language

query = 'Pantaloons'
#reads lat long from file
lat_lng_df=pd.read_excel('C:\\Users\\sachin.prabhu\\Desktop\\Google Reviews\\Trends\\lat_long.xlsx')
#lat_lng_df = lat_lng_df.iloc[:5,:] for testing only
df_final=pd.DataFrame() # df to write final file
df_temp=pd.DataFrame() #temp df to store individual store review

for site_code,lat,lng in zip(lat_lng_df['store_code'],lat_lng_df['lats'],lat_lng_df['long']):


    try:
        if site_code and lat and lng: #null lat, lng values for some of the site codes
            print('getting reviews for site code',site_code)
            df_temp=get_review({'lat':lat,'lng':lng},query)
            df_temp['site_code']=site_code
            df_final = df_final.append(df_temp,sort=False)

    except ValueError:
        pass


score_reviews(df_final,'C:\\Users\\sachin.prabhu\\Desktop\\Google Reviews\\Trends\\review_scores_pantaloons.csv')
