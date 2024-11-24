import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
# df2 = pd.read_csv('auto-mpg.csv', delimiter=",")
# Content for the second column
with col1:
data = pd.read_csv('auto-mpg.csv', delimiter=",")  # Remplacez 'auto-mpg.csv' par le chemin réel du fichier

chart = alt.Chart(data).mark_rect().encode(
    alt.X("mpg:Q", bin=True),  # "mpg" est la colonne pour l'histogramme, bin=True crée des bins
    alt.Y('count()', stack=None)  # "count()" compte les valeurs dans chaque bin
).properties(
    title='Histogramme de mpg'
)

st.altair_chart(chart, use_container_width=True)
#-------------------------------------------------------------------------------------
# Content for the first column
with col2:
data_aggregated = data.groupby('mpg').size().reset_index(name='count')
            
            # 2. Create the Donut Chart
donut_chart = alt.Chart(data_aggregated).mark_arc(innerRadius=50).encode(
theta='count:Q',  # Angle of the donut slice (based on 'count')
color='mpg:N',  # Color of the slice (based on 'Species')
tooltip=['mpg:N', 'count:Q']  # Tooltip shows Species and count
    ).properties(
    title='Distribution des espèces dans la Dataset',
    width=400,
    height=400
            )
st.altair_chart(donut_chart, use_container_width=True)
#----------------------------------------------------------------------

with st.sidebar:
    st.title('DASHBOARD')

