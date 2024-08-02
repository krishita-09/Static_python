import pandas as pd 

def save_to_csv(data, f_name='Clean_Covid_Data.csv'):   #function to save the dataset to a file specified
    data.to_csv(f_name, index=False)    #save .csv file for the data without index column i.e. index = False, rows will not be indexed 
    print(f'Saved cleaned data to {f_name}')

def load_from_csv(f_name='Clean_Covid_Data.csv'):   #function to load data
    try:
        df = pd.read_csv(f_name)
        if df.empty == True:
            raise ValueError("No data found in the CSV file")
        return df
    except FileNotFoundError as e:
        raise e
    except pd.errors.EmptyDataError:
        raise ValueError("Empty CSV file")
    except Exception as e:
        raise e
