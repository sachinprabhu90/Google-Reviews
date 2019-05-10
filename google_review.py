import googlemaps
import pprint
import time
import pandas as pd
import datetime
from googlemapsapikey import my_key






def get_review(lat_lng,query):

    '''
    Takes a lattitude and longitude pair and returns
    author_name, author_url, language, profile_photo_url, rating,
    relative_time_description, text(review), timestamp
    '''

    df_out = pd.DataFrame()

    if isinstance(lat_lng,dict):
        pass # just a failsafe
    else:
        print('please share the location as dict with keys as lat,lng')
        return

    API_KEY = my_key() # returns API KEY
    gmaps = googlemaps.Client(key=API_KEY) # creates session with Google Server

    places_result = gmaps.places(query=query,location = lat_lng,radius=1000,type='clothing_store')

    for place in places_result['results']:
         if place['name']=='Pantaloons':

            #define my place id
            my_place_id = place['place_id']

            #define the required fields
            my_fields = ['name','vicinity','type','review']

            #make request for details
            place_details = gmaps.place(my_place_id, fields=my_fields)


    try:
        for review in place_details['result']['reviews']:
                df=pd.DataFrame(review,index=range(1)) # dict is directly fed into df
                df_out=df_out.append(df)
    except KeyError:
        pass  #if review does not exist for a store, throws key error
    except UnboundLocalError:
        pass  # Occurs due to JSON dumped by API

    print('returned') # for console interaction only
    df_out.to_csv('before_cleaning.csv')
    return df_out
