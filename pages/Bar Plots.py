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
import random
random.seed(90)
diamond_df=diamond_df.loc[random.sample(list(range(len(df))),5000)].reset_index(drop=True)
df=df.loc[random.sample(list(range(len(df))),5000)].reset_index(drop=True)
st.subheader('The Bar plots of Diamond data')
v1_list = ['cut','color','clarity']
vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=4)
v2_list = list(df.columns)
vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=5)
title = f"The Bar plot of {vari1} and {vari2}"
fig4 = px.bar(diamond_df, x = vari1, y = vari2,title=title)
st.plotly_chart(fig4)
st.dataframe(pd.DataFrame(round(diamond_df.groupby(vari1)[vari2].mean(),2)).T)
