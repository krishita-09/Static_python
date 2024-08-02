# sl.subheader('Horizontal Bar')
# plt.figure()
# plt.barh(df[num].head(30).value_counts().index, df[num].head(30).value_counts().values)
# sl.pyplot(plt)



# def plot_total_cases(df):
#     try:
#         plt.figure(figsize=(15, 15))
#         df[['Confirmed', 'Deaths', 'Recovered']].sum().plot(kind='bar', color=['blue', 'red', 'green'])
#         plt.title('Total Cases: Confirmed, Deaths, and Recovered')
#         plt.xlabel('Case Type')
#         plt.ylabel('Total Count')
#         plt.xticks(rotation=0)
#         plt.savefig('total_cases.png')
#         plt.close()
#     except KeyError as e:
#         raise DataCleaningError(f"Missing key {e} in the dataset.")

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_total_cases(df):
    plt.figure(figsize=(15, 15))
    cases =df['Confirmed', 'Deaths', 'Recovered'].sum()
    plt.title('Total Cases: Confirmed, Deaths, and Recovered')
    plt.xlabel('Case Type')
    plt.ylabel('Total Count')
    plt.bar(cases.value_counts().index, cases.value_counts().values)
    plt.savefig('total_cases.png')
    st.pyplot(plt)

    
plot_total_cases('Clean_Covid_Data.csv')