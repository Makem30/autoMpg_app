import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np
import pandas as pd 
import altair as alt

# Charger les données
df2 = pd.read_csv('auto-mpg.csv', delimiter=",")
chart = alt.Chart(data).mark_bar().encode(x='MPG Bins' , y='Count').properties(
    title='Histogramme')
