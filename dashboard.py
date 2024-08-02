import streamlit as st
import matplotlib.pyplot as plt
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases
from file_handling import load_from_csv

def display_total_cases(df, case_type):
    st.subheader(f'Total {case_type} COVID-19 Cases')
    fig = plot_total_cases(df, case_type)
    st.pyplot(fig)

def display_top_countries(df, top_n):
    st.subheader(f'Top {top_n} Countries with Highest Number of COVID-19 Cases')
    fig = plot_top_countries(df, top_n)
    st.pyplot(fig)

def display_daily_cases(df):
    st.subheader('Daily New COVID-19 Cases')
    fig = plot_daily_cases(df)
    st.pyplot(fig)

def run_dashboard():
    st.title('COVID-19 Data Dashboard')

    try:
        df = load_from_csv('Clean_Covid_Data.csv')  # Load cleaned data

        st.sidebar.title('Filters')
        countries = ['Global'] + list(df['Country/Region'].unique())
        selected_country = st.sidebar.selectbox('Select a Country/Region', countries)

        if selected_country != 'Global':
            filtered_df = df[df['Country/Region'] == selected_country]
        else:
            filtered_df = df.groupby('Country/Region').sum().reset_index()

        case_types = ['Confirmed', 'Deaths', 'Recovered']
        selected_case_type = st.sidebar.selectbox('Select Case Type', case_types)

        if st.sidebar.button('Generate Plot'):
            if selected_case_type == 'Confirmed':
                display_total_cases(filtered_df, 'Confirmed')

            elif selected_case_type == 'Deaths':
                display_total_cases(filtered_df, 'Deaths')

            elif selected_case_type == 'Recovered':
                display_total_cases(filtered_df, 'Recovered')

            display_top_countries(df, 10)
            display_daily_cases(filtered_df)

    except FileNotFoundError:
        st.error("Data file not found.")
    except Exception as e:
        st.error(f"Error loading data: {e}")

