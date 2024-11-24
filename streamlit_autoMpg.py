import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
# df2 = pd.read_csv('auto-mpg.csv', delimiter=",")

data = pd.read_csv('auto-mpg.csv', delimiter=",")  # Remplacez 'auto-mpg.csv' par le chemin réel du fichier

chart = alt.Chart(data).mark_rect().encode(
    alt.X("mpg:Q", bin=True),  # "mpg" est la colonne pour l'histogramme, bin=True crée des bins
    alt.Y('count()', stack=None)  # "count()" compte les valeurs dans chaque bin
).properties(
    title='Histogramme de mpg'
)

st.altair_chart(chart, use_container_width=True)

with st.sidebar:
    st.title('DASHBOARD')

