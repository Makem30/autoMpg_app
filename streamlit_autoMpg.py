import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
data = pd.read_csv('auto-mpg.csv', delimiter=",")

