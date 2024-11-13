#!/usr/bin/env python
# coding: utf-8

# In[21]:


#%pip install streamlit
import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import html

#%pip freeze > "requirements.txt"

# Set the week number
week = 12


# In[19]:


# Set up directory and read in the data
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, 'data', f'Week {week}_no_outcomes.xlsx')

# Load data
df = pd.read_excel(data_path)
df = df.sort_values(by='home_team')

# Generate list of games
df['game_for_list'] = [f"{away} @ {home}" for home, away in zip(df['home_team'], df['away_team'])]

# Page title
st.title(f'Week {week} games and predictions')

# Selection box to choose game
selected_game = st.selectbox('Game: ', df['game_for_list'])

df2 = df[df['game_for_list']==selected_game]


# In[20]:


# Example data
# Assuming 'df2' contains columns 'home_team', 'Probability of home win', 'Upper bound of probability', and 'Lower bound of probability'
home_team = df2['home_team'].iloc[0]
away_team = df2['away_team'].iloc[0]
prediction = df2['Probability of home win'].iloc[0]
upper = df2['Upper bound of probability'].iloc[0]
lower = df2['Lower bound of probability'].iloc[0]
home_moneyline = df2['home_moneyline']
away_moneyline = df2['away_moneyline']

# Initialize the figure
fig = go.Figure()

# Add horizontal bar representing the home team win probability only
fig.add_trace(go.Bar(
    x=[prediction],
    y=[f"{home_team} Win Probability"],
    orientation='h',
    marker=dict(color='#66b3ff'),
    showlegend=False
))


# Add an annotation just above the edge of the bar
fig.add_annotation(
    x=prediction,
    y=0,
    text=f"{prediction:.0%}",
    showarrow=False,
    yshift=55,  # Adjusts the text position above the bar,
    font=dict(color="black")
)


# Add dotted lines for upper and lower estimates
fig.add_shape(
    type="line",
    x0=upper, x1=upper,
    y0=-0.5, y1=0.5,
    line=dict(color="red", width=2, dash="dot"),
)

fig.add_shape(
    type="line",
    x0=lower, x1=lower,
    y0=-0.5, y1=0.5,
    line=dict(color="green", width=2, dash="dot"),
)

# Add annotations for upper and lower estimates
fig.add_annotation(
    x=upper,
    y=0,
    text=f"Upper-bound: {upper:.0%}",
    showarrow=True,
    arrowhead=2,
    ax=55, ay=-30,
    font=dict(color="red")
)

fig.add_annotation(
    x=lower,
    y=0,
    text=f"Lower-bound: {lower:.0%}",
    showarrow=True,
    arrowhead=2,
    ax=-55, ay=-30,
    font=dict(color="green")
)

# Set layout with percentage formatting on x-axis
fig.update_layout(
    title=f"Predicted Probability of Home Team ({home_team}) Win",
    xaxis=dict(range=[-.19, 1.19], title="Probability", tickformat=".0%"),
    height=300,
    yaxis=dict(showticklabels=True)
)

if int(home_moneyline)>0:
    home_moneyline = "+" + str(int(home_moneyline))
else:
    home_moneyline = str(int(home_moneyline))

if (prediction>.5 and lower>.5) or (prediction<.5 and upper<.5):
    st.html(f"<p>{home_team} ({home_moneyline}) has a <b><span style='font-size:125%;'>{prediction:.0%}</span></b> chance of winning, with a lower-bound estimate of <span style='color:red;'>{lower:.0%}</span> and an upper-bound estimate of <span style='color:green;'>{upper:.0%}</span>.</p>")
else:
    st.html(f"<p>This game is projected as a <b><span style='font-size:125%;'>toss-up</span></b>.</p>")

# Display the chart in Streamlit
st.plotly_chart(fig)


# In[ ]:




