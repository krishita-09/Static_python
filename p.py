import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("combined.csv")

print(df.info())

print(df.isna().sum())

print(df.duplicated().sum())

df.drop(['review_url'], axis = 1, inplace = True)

print(df.info())

df.drop_duplicates(inplace = True)

print(df.duplicated().sum())

df.to_csv('clean_movie_data.csv', index = False)


# print(df['rating'].value_counts())

# # print(df.groupby('year').index().values())
# # 1915 - 2020

# print(df.shape)
# # (1392, 9)

# print(df.describe)

# print(df.genres.describe)

# # agegroup = df.groupby('movie_rated').count()

# # plt.figure(figsize=(10,10))
# # plt.plot(agegroup, 'g--')
# # plt.xlabel('Age categories')
# # plt.ylabel('Number of movies')
# # st.pyplot(plt)

# yeargroups = df['year'].unique()

# print(yeargroups)


