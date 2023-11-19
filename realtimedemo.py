import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
#importing all the required libraries
def app():
    #reading data
    df = pd.read_csv('archive/targetandvariabledatafinal.csv')
    df['date'] = pd.to_datetime(df['date'])

    #defining containers
    header = st.container()
    plot_spot = st.empty()
    placeholder = st.empty()

    #title
    with header:
        st.markdown("<h2 style='text-align: center; color: black;'>Real-Time Prediction</h1>", unsafe_allow_html=True)


    #func call


    col03,col04 = st.columns(2)
        
    with col03:
        with header : 
            #st.write("""### Reactor Inlet Parameters""")
            st.markdown("<h4 style='text-align: justify; color: black;'> Reactor Inlet Parameters</h1>", unsafe_allow_html=True)

            param_lst = list(df.columns)
            param_lst.remove('date')
            param_lst.remove('Concentration Propylene Glycol Outlet Reactor')
            param_lst.remove('Vapour Product Flow Outlet Reactor')
            param_lst.remove('Liquid Product Flow Outlet Reactor')
            select_param1 = st.selectbox('The Left side graph',   param_lst, key="affandry")
            
    with col04:
        with header : 
            #st.write("""### Predicted Reactor Outlet""")
            st.markdown("<h4 style='text-align: justify; color: black;'> Predicted Reactor Outlet</h1>", unsafe_allow_html=True)
            
            param_2st = list(df.columns)
            param_2st.remove('date')
            param_2st.remove('Liquid Percent Level in Reactor')
            param_2st.remove('Reactor Temperature')
            param_2st.remove('Reactor Internal Pressure')
            param_2st.remove('Water Volume Flow to Reactor')
            param_2st.remove('Propylene Oxide Volume Flow to Reactor')
            param_2st.remove('Nitrogen Flow to Reactor')
            select_param2 = st.selectbox('The Right side graph',   param_2st,  key="taufik")

    n = len(df)

    col01,col02 = st.columns(2)

    with plot_spot:
                
        with col01: 

            with placeholder.container() :
                
                def make_chart(df, y_col, ymin, ymax):
                    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
                    fig.add_trace(go.Scatter(x=df['date'], y=df[y_col],           mode='lines+markers'))
                    fig.update_layout(width=700, height=570, xaxis_title='time',
                    yaxis_title=y_col)
                    st.write(fig)
                        
        with col02:

                
            with placeholder.container() :

                def make_chart(df, y_col, ymin, ymax):
                    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
                    fig.add_trace(go.Scatter(x=df['date'], y=df[y_col],           mode='lines+markers'))
                    fig.update_layout(width=700, height=570, xaxis_title='time',
                    yaxis_title=y_col)
                    st.write(fig)
                    
        for i in range(0, n-30, 1):
            df_tmp = df.iloc[i:i+30, :]
            
            with st.container():
                col1,col2 = st.columns(2)
                with col1:
                    ymax = (df[select_param1])+10
                    ymin = min(df[select_param1])-10
                    make_chart(df_tmp, select_param1, ymin, ymax)
                
                with col2:
                    ymax = (df[select_param2])+10
                    ymin = min(df[select_param2])-10
                    make_chart(df_tmp, select_param2, ymin, ymax)
                
            time.sleep(0.1)



