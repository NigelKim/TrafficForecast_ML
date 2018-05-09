## Weekly Forecast of Fastest Driving Route with Historical Traffic and Weather Data

Seunghwan “Nigel” Kim, Dohoon “Andy” Kim

Advisor: Dr. Sanmay Das

Spring 2018 CSE 400E Report

Washington University in St. Louis

https://github.com/NigelKim/TrafficResearch

   We live in a world where driving is the standard way of transportation. Accordingly, various map service providers make use of massive traffic data and metadata to predict the real-time fastest driving route between two specific geographic coordinates, often also known as ‘navigation services’.  It collects real-time traffic information and optimizes the shortest path to the endpoint with shortest time.
   
  However, predicting a future time’s fastest driving route has not been as fast growing; Google Maps launched a service on December 2017 that predicts the fastest driving route for only a 3-hour future timeframe. If extended to a further timeframe, 24-hour daily prediction or a 7-day weekly prediction becomes possible.
  
   In this study, we integrate historical weather metadata with historical traffic congestion data to train suitable machine learning algorithms and perform a statistical test to assess the performance. Then, with the optimal model, we make prediction about a specified day of the week and ultimately, predict a future 7-day timeframe’s fastest driving routes similarly to a commonly known 7-day weather forecast.

References

[1]	Google Maps Directions API. https://developers.google.com/maps/documentation/directions/intro 
[2]	Bing Maps REST Services API. https://msdn.microsoft.com/en-us/library/ff701713.aspx 
[3]	Chicago Data Portal. “Chicago Traffic Tracker - Historical Congestion Estimates by Segment - 2011-2018.” https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/77hq-huss 
[4]	Chicago Data Portal. “Chicago Traffic Tracker - Congestion Estimates by Segments.” https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Congestion-Estimates-by-Se/n4j6-wkkf 
[5]	OpenWeatherMap. Chicago Weather History Bulk(2012/10-2018/3). JSON file. 
[6]	Melissa J.Azur, Elizabeth A. Stuart, Constantine Frangakis, Philip J. Leaf. (2011) “Multiple imputation by chained equations: what is it and how does it work?”
[7]	Divya Ramani, Harshita Kanani, Chirag Pandya. (2013) “Ensemble of classifiers based on association rule mining”
[8]	S.B. Kotsiantis. (2007) “Supervised machine learning: a review of classification techniques”
