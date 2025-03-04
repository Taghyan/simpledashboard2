
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout = 'wide', page_title = 'Dashboard')

tab1, tab2 = st.tabs(['Descriptive statistics', 'Charts'])

df = px.data.tips()
num = df.describe()
cat = df.describe(include= 'O')

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Numerical discriptive statistics')
        st.dataframe(num)
    with col3:
        st.subheader('Categorical discriptive statistics')
        st.dataframe(cat)

with tab2:
    day = st.sidebar.selectbox('Select the Day', df['day'].unique())
    time = st.sidebar.selectbox('Select the Time', df['time'].unique())
    col1, col2, col3 = st.columns(3)
    with col1:
        new_df = df[df['day'] == day]
        fig = px.histogram(new_df, x= 'total_bill', color= 'sex', title= f'total bills of {day}day'.title())
        st.plotly_chart(fig, use_container_width= True)
        fig = px.bar(new_df, x= 'time', y= 'total_bill', color= 'sex', barmode= 'group', title= f'time and total bills for {day}day'.title())
        st.plotly_chart(fig, use_container_width= True)

    with col3:
        new_df2 = df[df['time'] == time]
        fig2 = px.scatter(new_df2, x= 'total_bill', y= 'tip', color= 'sex', title= f"correlation between tips and total bills at {time}".title())
        st.plotly_chart(fig2, use_container_width= True)
        fig2 = px.bar(new_df2, x= 'day', y= 'total_bill', color= 'sex', title= f"day and total bills at {time}".title())
        st.plotly_chart(fig2, use_container_width= True)
