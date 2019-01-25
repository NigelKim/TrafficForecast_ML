## Machine Learning Application Project: Weekly Forecast of Fastest Driving Route with Historical Traffic and Weather Data ##

Topic: Week-long Hourly Traffic Forecast using historical traffic data and ML algorithms


Members:\
Seunghwan "Nigel" Kim    (seunghwan.kim@wustl.edu)\
Dohoon "Andy" Kim        (dohoon.kim@wustl.edu)

Language: *Python, PHP, SQL, HTML*\
Course: CSE400E Independent Study\
Independent Study Advisor : Sanmay Das Ph.D.\
Institution: Washington University In St. Louis\
Time: Spring 2018



   We live in a world where driving is the standard way of transportation. Accordingly, various map service providers make use of massive traffic data and metadata to predict the real-time fastest driving route between two specific geographic coordinates, often also known as ‘navigation services’.  It collects real-time traffic information and optimizes the shortest path to the endpoint with shortest time.
   
  However, predicting a future time’s fastest driving route has not been as fast growing; Google Maps launched a service on December 2017 that predicts the fastest driving route for only a 3-hour future timeframe. If extended to a further timeframe, 24-hour daily prediction or a 7-day weekly prediction becomes possible.
  
   In this study, we integrate historical weather metadata with historical traffic congestion data to train suitable machine learning algorithms and perform a statistical test to assess the performance. Then, with the optimal model, we make prediction about a specified day of the week and ultimately, predict a future 7-day timeframe’s fastest driving routes similarly to a commonly known 7-day weather forecast.

For our study, origin and endpoint were arbitrarily selected according to our four initial policies:
1.	Selected pair must have more than one competitive output class.
2.	Pair must be in a geographical region where we can obtain historical records of fastest driving route.
3.	Pair must be in a region where we can access the historically measured congestion information in detail.
4.	Pair must be in a region where we can acquire further metadata that can indirectly serve as input features.

Origin (geocoordinates)	John Hancock Center, IL (41.898811, -87.623077)\
Endpoint (geocoordinates) Taste of Randolph, IL (41.884276, -87.652300)\
Distance (km)	5.168\
Duration (s)	592

Raw dataset after collection:\
Number of data points: 2038  (historical data from 2011/10/01-2018/4/30)\
Index:\
datetime  (format: XX/XX/20XX)\
day          (format: ‘Mon’, ‘Tue’, etc.)\
Features:\
	congestion  (format: label)\
	congestionSpeed  (format: integer)\
	warningcounts  (format: integer)\
	weather condition  (format: string)\
	temperature  (format: real value, in degrees Celcius)\
	windspeed  (format: real value, in mi/h)\
Output:\
	routeoption   (format: positive integer multiclass output)

### Please read CSE400E_Report_Seunghwan Kim_Dohoon Kim.docx for more information regarding our project. ###


References

[1]	Google Maps Directions API. https://developers.google.com/maps/documentation/directions/intro 
[2]	Bing Maps REST Services API. https://msdn.microsoft.com/en-us/library/ff701713.aspx 
[3]	Chicago Data Portal. “Chicago Traffic Tracker - Historical Congestion Estimates by Segment - 2011-2018.” https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/77hq-huss 
[4]	Chicago Data Portal. “Chicago Traffic Tracker - Congestion Estimates by Segments.” https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Congestion-Estimates-by-Se/n4j6-wkkf 
[5]	OpenWeatherMap. Chicago Weather History Bulk(2012/10-2018/3). JSON file. 
[6]	Melissa J.Azur, Elizabeth A. Stuart, Constantine Frangakis, Philip J. Leaf. (2011) “Multiple imputation by chained equations: what is it and how does it work?”
[7]	Divya Ramani, Harshita Kanani, Chirag Pandya. (2013) “Ensemble of classifiers based on association rule mining”
[8]	S.B. Kotsiantis. (2007) “Supervised machine learning: a review of classification techniques”
