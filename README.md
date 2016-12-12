# Analysis of Dangerous Crimes in Boston
CS505 Computational Tools for Data Science

By Jacquelyn Andrade, Yao Zhang

## Abstract:
In our project we analyze the types of crime that occur in given locations around Boston on specific times of day. We perform K-means clustering on our data to classify our districts by the most popular crime. After performing this technique, we provide an in-depth review of particular statistics of crime that occur within a day, and whether time can indeed be used to classify the occurrence of a crime in a district. We use regression techniques to be able to predict the amount of occurrences of a specific crime as well as the probability of the crime occurring out of all crimes within a district. We expect our findings to closely correlate to “typical” crimes associated with certain times of the day. For example, we do not expect to find a substantial amount of crimes such as DUI in the morning, whereas robberies are more likely to occur at any time of day.

## Scripts:
`script.ipynb` takes the dataset crime_incident_report_august_2015_to_date.csv obtained from City of Boston.gov, transforms and filters out data not relevant to our study, and generates cleaned_crime_data.csv that is used by `regression.py` and `clustering_script.ipynb`.

`regression.py` performs Linear and Logistic Regression on the data points.  `clustering_script.ipynb` clusters and categorizes the data points.

`service.py` is our prototype web-service that visualizes the results obtained from the algorithm scripts.
