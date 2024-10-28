#!/usr/bin/env python
# coding: utf-8

# In[8]:


#%pip install streamlit
import streamlit as st
import pandas as pd
import os

# Set the week number
week = 10


# In[4]:


# Set up directory and read in the data
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, 'data', f'Week {week}_no_outcomes.xlsx')

# Load data
df = pd.read_excel(data_path)

# Generate list of games
df['game_for_list'] = [f"{away} @ {home}" for home, away in zip(df['home_team'], df['away_team'])]

# Page title
st.title(f'Week {week} games and predictions')

# Selection box to choose game
selected_game = st.selectbox('Game: ', df['game_for_list'])


# In[5]:


#To push as .py file
#jupyter nbconvert --to script "C:\Users\Lucas\OneDrive\python\College football\Streamlit application\Streamlit_cfb.ipynb"


#To push a file to github via pycharm terminal
#cd "C:\Users\Lucas\OneDrive\python\College football\Streamlit application"
#git init
#git remote remove origin
#git remote add origin https://github.com/lmisera/cfb_predictions
#git add "C:\Users\Lucas\OneDrive\python\College football\Streamlit application"
#git commit -m "Add initial file"
#git push -u origin main

