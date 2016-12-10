
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt

# day map used to convert days to numbers for linear regression
DAY_MAP = {'Sunday': 1,           'Monday': 2,           'Tuesday': 3,           'Wednesday': 4,           'Thursday': 5,           'Friday': 6,           'Saturday': 7}


def predictAmountCrimes(district, type_crime, user_day):
    crime = ""

    for i in type_crime:
        if i == ".":
            crime += "/"
        elif i == "_":
            crime += " "
        else:
            crime += i

    type_crime = crime
    print(type_crime)

    user_day = int(user_day)
    df = pd.read_csv('cleaned_crime_data.csv')
    
    # look at only data relevant to this district
    df_district = df[df['district'] == district]
    
    # get all possible hours and days of the week 
    hours = list(set(df_district['hour'].tolist()))
    days_of_week = list(set(df_district['day_of_week'].tolist()))
    
    # iterate through filtered dataframes to find when and how much the specified crimes occur
    relation_list = []
    for day in days_of_week:
        df_by_day = df_district[df_district['day_of_week'] == day]
        for hour in hours: 
            df_by_day_hour = df_by_day[df_by_day['hour'] == hour]
            count = 0
            for ind, row in df_by_day_hour.iterrows():
                if row['offense_type'] == type_crime:
                    count += 1
                relation_list.append({'hour': hour, 'day': DAY_MAP[day],'total_crimes': count})
    
    # convert to a dataframe to do linear regression as a predictor for total occurences of that crime
    df_crimes = pd.DataFrame.from_records(relation_list)
    
    # if nothing was found in the dataframe do do regression
    if not df_crimes.shape[0]:
        return 0
    else: 
        # perform multiple linear regression
        res = smf.ols(formula="total_crimes ~ day + hour", data=df_crimes).fit()
#         print(res.summary())
        
        # make a prediction based upon the day and hour for a specific crime within a district
        day_predictions = []
        for i in range(24):
            day_predictions.append(res.predict(exog={'day':user_day, 'hour':i})[0])
        return [type_crime] + day_predictions


def predictProbabilityOfCrime(district, type_crime, user_day):

    crime = ""

    for i in type_crime:
        if i == ".":
            crime += "/"
        elif i == "_":
            crime += " "
        else:
            crime += i

    type_crime = crime
    print(type_crime)

    user_day = int(user_day)
    
    # flag to avoid Perfect Seperation error (when all is_crime is either 0 or 1)
    not_available = True

    df = pd.read_csv('cleaned_crime_data.csv')
    
    # filter inital df with the specified district
    df_district = df[df['district'] == district]
    
    # find all possible hours and days for this district
    hours = list(set(df_district['hour'].tolist()))
    days_of_week = list(set(df_district['day_of_week'].tolist()))
    
    # iterate through filtered dataframes to find when the exact crimes occured in comparison to other crimes
    relation_list = []
    for day in days_of_week:
        df_by_day = df_district[df_district['day_of_week'] == day]
        for hour in hours: 
            df_by_day_hour = df_by_day[df_by_day['hour'] == hour]
            for ind, row in df_by_day_hour.iterrows():
                is_crime = 0
                if row['offense_type'] == type_crime:
                    not_available = False # switch to false, results are varied now
                    is_crime = 1    
                relation_list.append({'is_crime': is_crime, 'hour': row['hour'], 'day': DAY_MAP[row['day_of_week']]})
    
    # convert to a dataframe to perform logistic regression
    df_crimes = pd.DataFrame.from_records(relation_list)
    
    # if variation in is_crimes not found do not perform regression
    if not_available:
        return 0
    else:
        # get the logistic model
        attribute_cols = df_crimes.columns[:2]
        logit = sm.Logit(df_crimes['is_crime'], df_crimes[attribute_cols])
        result = logit.fit()
#         print(result.summary())
        
        prediction_day=[]
        # make a prediction
        for i in range(24):
            prediction_day.append(result.predict([user_day, i])[0])
            
        return [type_crime] + prediction_day




