import streamlit as st
import pandas as pd
import numpy as np 
 
 st.title("voulez vous")
 st.write("ive been there for you")
 st.write(" and im all out of love")
 st.write(pd.dataframe({
     'first column': [1,2,3,4],
     'second column':[10,20,30,40]
 }))
 map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
