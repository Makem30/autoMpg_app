import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np


# Charger les données
# df2 = pd.read_csv('auto-mpg.csv', delimiter=",")
# Content for the second column

data = pd.read_csv('auto-mpg.csv', delimiter=",")  # Remplacez 'auto-mpg.csv' par le chemin réel du fichier

# Create two columns
col1, col2 = st.columns([0.5,0.4],gap="large")

with col1:
  chart = alt.Chart(data).mark_rect().encode(
  alt.X("mpg:Q", bin=True),  # "mpg" est la colonne pour l'histogramme, bin=True crée des bins
  alt.Y('count()', stack=None)  # "count()" compte les valeurs dans chaque bin
                  ).properties(
                          title='Histogramme de mpg'
                          )
                          
  st.altair_chart(chart, use_container_width=True)
#-------------------------------------------------------------------------------------
#Content for the first column
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

# Charger les données
# data = pd.read_csv('auto-mpg.csv')

# Créer la sidebar
st.sidebar.title("Comparateur de données")

# Sélection des données à comparer
x_axis = st.sidebar.selectbox("Axe des x", ["mpg", "cylinders", "weight", "acceleration"])
y_axis = st.sidebar.selectbox("Axe des y", ["mpg", "cylinders", "weight", "acceleration"], index=1)  # index=1 pour sélectionner "cylinders" par défaut

# Créer le graphique
chart = alt.Chart(data).mark_point().encode(
    x=x_axis,
    y=y_axis,
    color='origin:N'  # Colorer les points par origine
).properties(
    title=f"Comparaison de {x_axis} et {y_axis}"
)

# Afficher le graphique
st.altair_chart(chart, use_container_width=True)
#------------------------------------------------------------------------------------------




# Create the sidebar
st.sidebar.title("Comparaison mpg vs car")

# Select cars to compare
selected_cars = st.sidebar.multiselect(
    "Selectionner les voitures à comparer:",
    data['car name'].unique(),
    default=data['car name'].unique()[:10]  # Select first 10 cars by default
)

# Filter data based on selected cars
filtered_data = data[data['car name'].isin(selected_cars)]

# Create the bar chart
chart = alt.Chart(filtered_data).mark_bar().encode(
    x='car name:N',
    y='mpg:Q',
    color='origin:N'
).properties(
    title="comparaison des voiture en fonction du mpg",
    width=600  # Adjust width as needed
)

# Display the chart
st.altair_chart(chart, use_container_width=True)

