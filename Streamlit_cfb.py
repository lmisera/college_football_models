#!/usr/bin/env python
# coding: utf-8

# In[28]:


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
#%pip install pipreqs
import pipreqs
#pipreqs > "C:/Users/Lucas/OneDrive/python/College football/Streamlit application/requirements.txt"

week = 10


# In[6]:


#Set up directory, read in week
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, 'data', f'Week {week}_no_outcomes.xlsx')

#get list of games
list_of_games = []
for home, away in zip(df['home_team'],df['away_team']):
    list_of_games.append(f"{away} @ {home}")

df['game_for_list'] = list_of_games

#Page title
st.title(f'Week {week} games and predictions')

#Selection box to choose game
selected_game = st.selectbox('Game: ', df['game_for_list'])


# In[ ]:


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

