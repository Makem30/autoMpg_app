import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
df2 = pd.read_csv('auto-mpg.csv', delimiter=",")

chart = alt.Chart(data).mark_bar().encode(x='mpg' , y='mpg').properties(
    title='Sepal Histogramme')

