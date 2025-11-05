import streamlit as st
import pickle
import pandas as pd

team = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Jaipur', 'Chennai',
       'Kolkata', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Dharamsala', 'Pune', 'Hyderabad', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Cuttack', 'Visakhapatnam', 'Rajkot', 'Kanpur',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

pipe = pickle.load(open('pikle.pkl','rb'))

st.title("IPL Win Predictor")

col1, col2 = st.columns(2)

with col1: 
    batting_team = st.selectbox("Select the batting team: ", sorted(team))

with col2: 
    bowling_team = st.selectbox('Select the bowling team: ', sorted(team))

selected_city = st.selectbox("select hosted city ", sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)
with col3: 
    score = st.number_input('Score')
with col4: 
    over = st.number_input('Overs Completed')
with col5: 
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target-score
    balls_left = 120 -(over*6)
    wickets = 10-wickets
    crr = score/over
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],"bowling_team":[bowling_team], 'city': [selected_city], 'runs_left':[runs_left],'balls_left':[balls_left], 'wickets':[wickets], 'total_runs_x':[target], 'crr':[crr],'rrr':[rrr]})
    
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header("Winnig Probability of each team: ")
    st.text(batting_team + ": " + str(round(win*100)) + "%")
    st.text(bowling_team + ": " + str(round(loss*100)) + "%")
