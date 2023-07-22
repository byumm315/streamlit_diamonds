import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
diamond_df=pd.read_csv('diamonds.csv')
diamond_df=diamond_df.drop('Unnamed: 0',axis=1) #Unnamed: 0 변수 삭제하기
diamond_df=diamond_df.drop(diamond_df[(diamond_df["x"]==0)|(diamond_df["y"]==0)|(diamond_df["z"]==0)].index).reset_index(drop=True) #x, y, z 셋 중 하나라도 0인 행은 삭제하였다.
df = diamond_df.drop(['cut','color','clarity'],axis=1)

diamond_df = diamond_df[(diamond_df["depth"]<75)&(diamond_df["depth"]>45)]
diamond_df = diamond_df[(diamond_df["table"]<80)&(diamond_df["table"]>40)]  
diamond_df = diamond_df[(diamond_df["x"]<30)]
diamond_df = diamond_df[(diamond_df["y"]<30)]
diamond_df = diamond_df[(diamond_df["z"]<30)&(diamond_df["z"]>2)]

df = diamond_df.drop(['cut','color','clarity'],axis=1)

@st.cache_data(experimental_allow_widgets=True)
def func6():
    global diamond_df
    st.subheader('The 3D Scatter Plots of Diamond data')
    diamond_df=diamond_df.sort_values(by='x').reset_index(drop=True)
    a,b = st.select_slider(f'Choose a x-axis point', options=sorted(diamond_df['x']),value=(np.min(sorted(list(set(diamond_df['x'])))),np.max(sorted(list(set(diamond_df['x']))))))
    k1=list(diamond_df[diamond_df['x']==a].index)[0]
    k2=list(diamond_df[diamond_df['x']==b].index)[-1]
    trace1 = go.Scatter3d(
            x = diamond_df.loc[k1:k2,'x'], y = diamond_df.loc[k1:k2,'y'],z = diamond_df.loc[k1:k2,'z'],
            mode = 'markers',
            marker = dict(size=3, color='blue'),
            )

    fig7 = go.Figure(data=[trace1])
    fig7.update_layout(
            scene = dict(
            xaxis_title = 'x-axis',
            yaxis_title = 'y-axis',
            zaxis_title = 'z-axis'),
            margin=dict(r=20, b=10, l=10, t=10),
        )

    st.plotly_chart(fig7, use_container_width=True)


@st.cache_data(experimental_allow_widgets=True)
def func7():
    global diamond_df
    diamond_df=diamond_df.sort_values(by='y').reset_index(drop=True)
    a,b = st.select_slider(f'Choose a y-axis point', options=sorted(diamond_df['y']),value=(np.min(sorted(list(set(diamond_df['y'])))),np.max(sorted(list(set(diamond_df['y']))))))
    k1=list(diamond_df[diamond_df['y']==a].index)[0]
    k2=list(diamond_df[diamond_df['y']==b].index)[-1]
    trace1 = go.Scatter3d(
            x = diamond_df.loc[k1:k2,'x'], y =diamond_df.loc[k1:k2,'y'],z = diamond_df.loc[k1:k2,'z'],
            mode = 'markers',
            marker = dict(size=3, color='blue'),
            )

    fig8 = go.Figure(data=[trace1])
    fig8.update_layout(
            scene = dict(
            xaxis_title = 'x-axis',
            yaxis_title = 'y-axis',
            zaxis_title = 'z-axis'),
            margin=dict(r=20, b=10, l=10, t=10),
        )

    st.plotly_chart(fig8, use_container_width=True)

@st.cache_data(experimental_allow_widgets=True)
def func8():
    global diamond_df
    diamond_df=diamond_df.sort_values(by='z').reset_index(drop=True)
    a,b = st.select_slider(f'Choose a z-axis point', options=sorted(diamond_df['z']),value=(np.min(sorted(list(set(diamond_df['z'])))),np.max(sorted(list(set(diamond_df['z']))))))
    k1=list(diamond_df[diamond_df['z']==a].index)[0]
    k2=list(diamond_df[diamond_df['z']==b].index)[-1]
    trace1 = go.Scatter3d(
            x = diamond_df.loc[k1:k2,'x'], y = diamond_df.loc[k1:k2,'y'],z = diamond_df.loc[k1:k2,'z'],
            mode = 'markers',
            marker = dict(size=3, color='blue'),
            )

    fig9 = go.Figure(data=[trace1])
    fig9.update_layout(
            scene = dict(
            xaxis_title = 'x-axis',
            yaxis_title = 'y-axis',
            zaxis_title = 'z-axis'),
            margin=dict(r=20, b=10, l=10, t=10),
        )

    st.plotly_chart(fig9, use_container_width=True)

func6()
func7()
func8()
