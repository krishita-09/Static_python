import pandas as pd     #importing libraries required for the code
from exceptions import DataCleaningError
from file_handling import save_to_csv, load_from_csv

def clean_data(df):     #function to clean the dataset and return it for analyzing
    if df.empty == True:
        raise DataCleaningError("DataFrame is empty")   #raising a user defined exception if the dataset is empty 

    df.drop_duplicates(inplace=True)    #used to drop duplicate values present in teh dataset
    
    con_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths', 'New recovered', 'Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered', 'Confirmed last week', '1 week change', '1 week % increase']

    for col in con_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')   #used for converting the datatype, coerce means that if a value cannot be converted to numeric, instead of giving an error, the system will NaN(Not a Number)

    df.fillna(0, inplace=True)      #used to replace missing values(including the NaN values produced after conversion) with 0

    df['Country/Region'] = df['Country/Region'].str.title()     #converting to title case

    print('Data cleaned successfully')

    return df   #returning cleaned dataset for further analysis
