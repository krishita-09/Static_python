import pandas as pd
import streamlit as sl
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\KRISHUSEEMI\\krishi\\COURSE_ANALYSIS\\Dataset.csv')
print(df)
print(df.isna().sum())
print(df.duplicated().sum())

sl.title('EDA Drugs/Hospital')
sl.subheader('Original Dataset')
sl.write(df)
sl.write(df.shape)

sl.subheader('Null value')
print(df.isna().sum())
sl.subheader('Duplicated value')
print(df.duplicated().sum())

num = sl.selectbox('Choose one',df.columns, index=9)
# sl.write(df['avg'].value_counts().index)
# sl.write(df['avg'].value_counts().values)

sl.subheader('Bar')
sl.bar_chart(df[num].head(30), color = '#FFFFFF')

sl.subheader('Line')
sl.line_chart(df[num].head(30), color = '#90EE90')

sl.subheader('Scatter')
sl.scatter_chart(df[num].head(30), color = '#Ff0000')

plt.figure(figsize = [15,15])
plt.pie(df[num].head(30).value_counts().values, labels = df[num].head(30).value_counts().index, colors = ['red','orange','blue'], autopct = '%1.2f%%')
sl.pyplot(plt)

sl.subheader('Horizontal Bar')
plt.figure()
plt.barh(df[num].head(30).value_counts().index, df[num].head(30).value_counts().values)
sl.pyplot(plt)

sl.sidebar.title('Sidebar')
sl.sidebar.write(df.columns)

