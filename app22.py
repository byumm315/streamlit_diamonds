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

st.set_page_config(
    page_title="Scatter plots"
)
st.subheader('The Scatter plots of Diamond data')
@st.cache_data(experimental_allow_widgets=True)
def func1():   
    fig = px.scatter_matrix(df)
    fig.update_traces(marker={'size':3})
    st.plotly_chart(fig)
func1()

@st.cache_data(experimental_allow_widgets=True)
def func2():
    v1_list = list(df.columns)
    vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=1)
    v2_list = list(df.columns)
    vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=2)
    v3_list = ['cut','color','clarity']
    vari3 = st.selectbox(label = "Choose a Third Variable", options = v3_list,key=3)
    title = f"The scatter plot of {vari1} and {vari2} with {vari3}"
    fig1 = px.scatter(diamond_df, x=vari1, y=vari2, color=vari3,title=title)
    fig1.update_traces(marker={'size':10})
    st.plotly_chart(fig1)

func2()
