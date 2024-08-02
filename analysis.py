import pandas as pd     #importing to use data, classes and functions of library or module
import streamlit as st
import matplotlib.pyplot as plt
from file_handling import load_from_csv, save_to_csv
from data_cleaning import clean_data
from exceptions import DataCleaningError
from dashboard import run_dashboard

try:
    content = pd.read_csv('covid_19_data.csv')

    cleaned_data = clean_data(content)
    save_to_csv(cleaned_data, 'Clean_Covid_Data.csv')

    #calculating 
    #using .loc to access all rows and columns and find maxinmum and minimum values present in column 'Confirmed'
    country_with_highest_cases = cleaned_data.loc[cleaned_data['Confirmed'].idxmax(), 'Country/Region']
    country_with_lowest_cases = cleaned_data.loc[cleaned_data['Confirmed'].idxmin(), 'Country/Region']

    # Display basics in terminal
    print('Analysis Results:')
    print('Total confirmed cases: ', cleaned_data['Confirmed'].sum())
    print('Total deaths: ', cleaned_data['Deaths'].sum())
    print('Total recovered cases: ', cleaned_data['Recovered'].sum())
    print(f"Highest cases in: {country_with_highest_cases}")
    print(f"Lowest cases in: {country_with_lowest_cases}")

    # Display basics using streamlit
    st.subheader('Analysis Results:')
    st.write('Total confirmed cases: ', cleaned_data['Confirmed'].sum())
    st.write('Total deaths: ', cleaned_data['Deaths'].sum())
    st.write('Total recovered cases: ', cleaned_data['Recovered'].sum())
    st.write(f'Highest cases in: {country_with_highest_cases}')
    st.write(f'Lowest cases in: {country_with_lowest_cases}')

    st.title('COVID-19 Data Dashboard')
    run_dashboard()  # Call the streamlit dashboard

    #plotting pie charts using streamlit and matplotlib
    plt.figure(figsize=[15, 15])
    plt.pie(cleaned_data['Deaths'].head(50).value_counts(), labels=cleaned_data['Deaths'].head(50).value_counts().index, colors=['red', 'yellow', 'blue', 'green', 'lightblue', 'lightgreen', 'purple', 'orange', 'grey'], autopct='%1.2f%%')
    plt.title('Pie Chart: Top 50 deaths distribution')
    st.pyplot(plt)

    plt.figure(figsize=[15, 15])
    plt.pie(cleaned_data['Confirmed'].head(50).value_counts(), labels=cleaned_data['Confirmed'].head(50).value_counts().index, colors=['red', 'yellow', 'blue', 'green', 'lightblue', 'lightgreen', 'purple', 'orange', 'grey'], autopct='%1.2f%%')
    plt.title('Pie Chart: Top 50 confirmed cases distribution')
    st.pyplot(plt)

    plt.figure(figsize=[15, 15])
    plt.pie(cleaned_data['Recovered'].head(50).value_counts(), labels=cleaned_data['Recovered'].head(50).value_counts().index, colors=['red', 'yellow', 'blue', 'green', 'lightblue', 'lightgreen', 'purple', 'orange', 'grey'], autopct='%1.2f%%')
    plt.title('Pie Chart: Top 50 recovered cases distribution')
    st.pyplot(plt)


except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Error: Missing key {e} in the dataset.")
except DataCleaningError as e:
    print(f"Error during data cleaning: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

