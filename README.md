COVID-19 Dataset Analysis Project
This project involves cleaning, analyzing, and visualizing COVID-19 data from the Kaggle dataset COVID-19 Dataset.
The given Dataset from kaggle provides us detailed information about the confirmed cases, deaths, and recoveries from the COVID-19 pandemic across various countries and regions and includes key metrics such as active cases, changes over time and recovery rates. This data is vital for knowing the global impact of the virus, aiding researchers, policymakers, and the public in tracking the progression of the pandemic and informing public health responses worldwide.

---------------Project Structure
The project is structured into several files:
1) data_cleaning.py (file for cleaningg data):
Uses pandas for loading and cleaning the dataset, handling missing values, correcting data types and ensures data consistency and reduce data redundancy.

2) file_handling.py (file for file handling purposes):
Provides functions to save the cleaned data to clean_covid_data.csv and to load the cleaned data from the CSV file.

3) exceptions.py (file for creating custom exception):
Defines a custom exception which can be raised during data cleaning process 

4) analysis.py (file for analyzing and calculating the data):
Performs basic analysis using pandas. Calculates total confirmed cases, deaths, and recovered cases. Displyas regions with the highest and lowest number of cases.
Visualizes distributions using pie charts for deaths, confirmed cases, and recovered cases.

5) visualization.py: Module for creating insightful visualizations using Matplotlib based on the cleaned COVID-19 data.

6) dashboard.py: Implements an interactive dashboard using Streamlit to display visualizations and allow user interaction.
---------------To run the code

Ensure Python is installed on your system along with the necessary libraries(streamlit, matplotlib, pandas).Install required libraries using pip:
pip install pandas matplotlib streamlit

Download the dataset from Kaggle.

Open a new terminal and write the following commands:
python data_cleaning.py
python analysis.py
These commands will clean the dataset, save it to clean_covid_data.csv, and perform analysis.

To view the charts write down 'streamlit run analysis.py' command in terminal

---------------Handling Custom Exceptions in data_cleaning.py:

class DataCleaningError(Exception):
    def __init__(self, message="Problem while trying to clean data"):
        self.message = message
        super().__init__(self.message)

The above snippet is present in the exceptions.py. This module is created to be imported to the other files and handle errors if they were to occur. A user defined exception which can be raised in other files where it is imported as a module for eg:


from exceptions import DataCleaningError

def clean_data(df):
    if df.empty ==True:
        raise DataCleaningError("DataFrame is empty")

    # Perform cleaning operations

    return df

The above code snippet present in data_cleaning.py raises a custom exception defined in file exceptions.py(which is imported). Thus allowing the system to be able to handle the error if a dataframe is empty and show the message to user


