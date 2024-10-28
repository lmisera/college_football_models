#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Display title and message
st.title("Streamlit Test")
st.write("Hello, this is a test to see if Streamlit is working!")

# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")
else:
    st.write("Button not clicked yet.")


# In[12]:


"""

#%pip install streamlit
import streamlit as st
import pandas as pd
import os

%pip freeze > "requirements.txt"

# Set the week number
week = 10

"""


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

