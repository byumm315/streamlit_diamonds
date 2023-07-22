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

st.set_page_config(
    page_title="Scatter plots - Remove outliers"
)
st.subheader('The Scatter plots of Diamond data')
@st.cache_data()
def func3():
    fig2 = px.scatter_matrix(df)
    fig2.update_traces(marker={'size':3})
    st.plotly_chart(fig2)
    st.subheader('The Correlation of Diamond data')
    st.dataframe(round(df.corr(),2))
func3()
