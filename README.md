# Google Reviews Scraping for Social Listening Tool

###Objective
-  To understand the customer sentiment regarding the Reliance Trends Stores among Google Local Guides and Reviewers.
   Reviews may be related to VM, merchandise, staff, parking etc.

###Methodology
-  Google Reviews are scraped using places API. Lat_Lang supplied to the API comes from the local file obtained from
   Ops Team storewise (/Files/lat_long.xlsx)
-  The review text are scored using nltk and have associated region and user info. The sample of scraped data can be
   found in /Files/score_sample.csv.

