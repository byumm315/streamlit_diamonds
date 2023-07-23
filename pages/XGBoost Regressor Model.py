import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import metrics

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

# Make copy to avoid changing original data 
label_data = diamond_df.copy()
object_cols=['cut','color','clarity']
# Apply label encoder to each column with categorical data
label_encoder = LabelEncoder()
for col in object_cols:
    label_data[col] = label_encoder.fit_transform(label_data[col])

dict_cut={}
aa=list(diamond_df[diamond_df['cut']=='Ideal'].index)[0]
dict_cut['Ideal']=label_data.loc[aa,'cut']
aa=list(diamond_df[diamond_df['cut']=='Premium'].index)[0]
dict_cut['Premium']=label_data.loc[aa,'cut']
aa=list(diamond_df[diamond_df['cut']=='Good'].index)[0]
dict_cut['Good']=label_data.loc[aa,'cut']
aa=list(diamond_df[diamond_df['cut']=='Very Good'].index)[0]
dict_cut['Very Good']=label_data.loc[aa,'cut']
aa=list(diamond_df[diamond_df['cut']=='Fair'].index)[0]
dict_cut['Fair']=label_data.loc[aa,'cut']

dict_color={}
aa=list(diamond_df[diamond_df['color']=='E'].index)[0]
dict_color['E']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='I'].index)[0]
dict_color['I']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='J'].index)[0]
dict_color['J']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='H'].index)[0]
dict_color['M']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='F'].index)[0]
dict_color['F']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='G'].index)[0]
dict_color['G']=label_data.loc[aa,'color']
aa=list(diamond_df[diamond_df['color']=='D'].index)[0]
dict_color['D']=label_data.loc[aa,'color']


dict_clarity={}
aa=list(diamond_df[diamond_df['clarity']=='SI2'].index)[0]
dict_clarity['SI2']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='SI1'].index)[0]
dict_clarity['SI1']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='VS1'].index)[0]
dict_clarity['VS1']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='VS2'].index)[0]
dict_clarity['VS2']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='VVS2'].index)[0]
dict_clarity['VVS2']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='VVS1'].index)[0]
dict_clarity['VVS1']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='I1'].index)[0]
dict_clarity['I1']=label_data.loc[aa,'clarity']
aa=list(diamond_df[diamond_df['clarity']=='IF'].index)[0]
dict_clarity['IF']=label_data.loc[aa,'clarity']



# Assigning the featurs as X and trarget as y
X= label_data.drop(["price"],axis =1)
y= label_data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=7)

xgb_model = xgboost.XGBRegressor()

xgb_model.fit(X_train,y_train)

import joblib

joblib.dump(xgb_model, "xgb.pkl")

import streamlit as st
import pandas as pd
import joblib

# Title
st.header("Streamlit Machine Learning App")

carat = st.number_input("Enter carat")
value = st.slider("values", 0, 10, step=0.001)
st.write(f"The Diamond Caret is {value}.")

depth = st.number_input("Enter depth")
value1 = st.slider("values", 30, 100, step=0.001)
st.write(f"The Diamond Depth is {value1}.")

table= st.number_input("Enter table")
value2 = st.slider("values", 30, 100, step=0.001)
st.write(f"The Diamond Table is {value2}.")

x= st.number_input("Enter X-axis")
value3 = st.slider("values", 0, 20, step=0.001)
st.write(f"The Diamond X-axis is {value3}.")

y = st.number_input("Enter Y-axis")
value4 = st.slider("values", 0, 20, step=0.001)
st.write(f"The Diamond Y-axis is {value4}.")

z= st.number_input("Enter Z-axis")
value5 = st.slider("values", 0, 20, step=0.001)
st.write(f"The Diamond Z-axis is {value5}.")


v1_list = list(set(diamon_df.cut))
vari1 = st.selectbox(label = "Choose a Cut Variable", options = v1_list,key=1)
st.write(f"The Diamond Cut is {vali1}.")

v2_list = list(set(diamon_df.color))
vari2 = st.selectbox(label = "Choose a Color Variable", options = v2_list,key=2)
st.write(f"The Diamond Color is {vari2}.")

v3_list = list(set(diamon_df.clarity))
vari3 = st.selectbox(label = "Choose a Clarity Variable", options = v3_list,key=3)
st.write(f"The Diamond clarity is {vali3}.")
