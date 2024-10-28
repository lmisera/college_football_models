#!/usr/bin/env python
# coding: utf-8

# In[16]:


#%pip install streamlit
import streamlit as st
import pandas as pd
import os

get_ipython().run_line_magic('pip', 'freeze > "requirements.txt"')

# Set the week number
week = 10

st.title("TEST")
st.write(f"AHHHHHHHHHH {week}")


# In[4]:


"""

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

"""

