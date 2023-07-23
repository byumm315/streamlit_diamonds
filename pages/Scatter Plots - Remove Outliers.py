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

v_list = list(df.columns)
vari = st.selectbox(label = "Choose a Variable", options = v_list,key=0)
diamond_df=diamond_df.sort_values(by=vari).reset_index(drop=True)
a,b = st.select_slider(f'Choose a {vari}-axis point', options=sorted(diamond_df[vari]),value=(np.min(sorted(list(set(diamond_df[vari])))),np.max(sorted(list(set(diamond_df[vari]))))))
k1=list(diamond_df[diamond_df[vari]==a].index)[0]
k2=list(diamond_df[diamond_df[vari]==b].index)[-1]
v1_list = list(df.columns)
vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=1)
v2_list = list(df.columns)
vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=2)
v3_list = ['cut','color','clarity']
vari3 = st.selectbox(label = "Choose a Third Variable", options = v3_list,key=3)
fig1 = px.scatter(diamond_df.loc[k1:k2], x=vari1, y=vari2, color=vari3,title=f'The Scatter plots of Diamond data({vari1,vari2,vari3})')
fig1.update_traces(marker={'size':10})
st.plotly_chart(fig1)
