import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile
from PIL import Image

#changing the page title and icon
img = Image.open('coolfire.png')
st.set_page_config(page_title = 'Wildire_AI', page_icon = img)
st.title('AI for Wildfire Mitigation')
base = "dark"

#hiding the menu button that is automatically integrated into the app
#hide_menu_style = """
	#<style>
	#MainMenu {visibility: hidden; }
	#footer {visibility: hidden; }
	#</style>
	#"""
#st.markdown(hide_menu_style, unsafe_allow_html=True)



# Display the backround image unsuccessfully 
#st.image("download.jpg", use_column_width=True)
# Apply CSS to set the image as the background for the entire Streamlit app
#st.markdown(
    #"""
    #<style>
    #.stApp {
        #background-image: url("https://drive.google.com/uc?id=11Hs9VUR_i-hyAoxDhXp38jUcwxHHCzyy");
        #background-size: cover;
    #}
    #</style>
    #""",
    #unsafe_allow_html=True
#)

# added blurb 
st.image('fireimage1.png')
#st.image('fireimage1.png', caption='Sunrise by the mountains')
st.subheader('Welcome to the forefront of wildfire spread simulation and mitigation.')
st.write("Our team's state-of-the-art research and simulation technology applies AI and reinforcement learning to optimize decision-making in wildfire mitigation, solving complex resource allocation problems.")

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app allow users to build a machine learning (ML) model in an end-to-end workflow. Particularly, this encompasses data upload, data pre-processing, ML model building and post-model analysis.')

  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, go to the sidebar and 1. Select a data set and 2. Adjust the model parameters by adjusting the various slider widgets. As a result, this would initiate the ML model building process, display the model results as well as allowing users to download the generated models and accompanying data.')

  st.markdown('**Under the hood**')
  st.markdown('Data sets:')
  st.code('''- Drug solubility data set
  ''', language='markdown')
  
  st.markdown('Libraries used:')
  st.code('''- Pandas for data wrangling
- Scikit-learn for building a machine learning model
- Altair for chart creation
- Streamlit for user interface
  ''', language='markdown')

# Sidebar for accepting input parameters
with st.sidebar:
    # Load data
    st.image('coolfire.png')
