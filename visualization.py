import pandas as pd
import matplotlib.pyplot as plt
from exceptions import DataCleaningError

def plot_total_cases(df):
    try:
        plt.figure(figsize=(12, 8))
        df[['Confirmed', 'Deaths', 'Recovered']].sum().plot(kind='bar', color=['blue', 'red', 'green'])
        plt.title('Total Cases: Confirmed, Deaths, and Recovered')
        plt.xlabel('Case Type')
        plt.ylabel('Total Count')
        plt.xticks(rotation=0)
        plt.savefig('total_cases.png')
        plt.close()
    except KeyError as e:
        raise DataCleaningError(f"Missing key {e} in the dataset.")

def plot_top_countries(df):
    try:
        top_countries = df.groupby('Country/Region')['Confirmed'].sum().nlargest(10)
        plt.figure(figsize=(12, 8))
        top_countries.plot(kind='bar')
        plt.title('Top 10 Countries with Highest Confirmed Cases')
        plt.xlabel('Country/Region')
        plt.ylabel('Confirmed Cases')
        plt.xticks(rotation=45)
        plt.savefig('top_countries.png')
        plt.close()
    except KeyError as e:
        raise DataCleaningError(f"Missing key {e} in the dataset.")

def plot_daily_cases(df):
    try:
        daily_cases = df['New cases']
        growth_rate = df['1 week % increase']
        dates = range(1, len(daily_cases) + 1)

        fig, ax1 = plt.subplots(figsize=(12, 8))

        ax1.bar(dates, daily_cases, color='b', alpha=0.6, label='Daily New Cases')
        ax1.set_xlabel('Days')
        ax1.set_ylabel('Daily Cases', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(dates, growth_rate, color='r', marker='o', linestyle='-', linewidth=2, label='Weekly Growth Rate (%)')
        ax2.set_ylabel('Weekly Growth Rate (%)', color='r')
        ax2.tick_params('y', colors='r')

        plt.title('Daily New Cases and Weekly Growth Rate')
        plt.savefig('daily_cases.png')
        plt.close()
    except KeyError as e:
        raise DataCleaningError(f"Missing key {e} in the dataset.")
