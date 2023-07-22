import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.title('Diamond Price Predictor') #홈페이지 제목추가
st.header('Diamond Data')
st.image('https://www.casadoro.com/wp-content/uploads/2022/03/diamond-980x654.jpeg')
diamond_df=pd.read_csv('C:/Users/tyumi/diamonds.csv')
diamond_df=diamond_df.drop('Unnamed: 0',axis=1) #Unnamed: 0 변수 삭제하기
diamond_df=diamond_df.drop(diamond_df[(diamond_df["x"]==0)|(diamond_df["y"]==0)|(diamond_df["z"]==0)].index).reset_index(drop=True) #x, y, z 셋 중 하나라도 0인 행은 삭제하였다.
st.write(diamond_df.head(20))
