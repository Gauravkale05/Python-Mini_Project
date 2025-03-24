import streamlit as st
import random

# Initialize session state for tracking wins
if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "comp_wins" not in st.session_state:
    st.session_state.comp_wins = 0

options = ["Rock", "Paper", "Scissors"]

st.title("Rock Paper Scissors Game")

user_pick = st.radio("Choose Rock, Paper, or Scissors:", options)

if st.button("Play"):
    comp_pick = random.choice(options)
    st.write(f"Computer Picked: {comp_pick}")
    
    if user_pick == "Rock" and comp_pick == "Scissors":
        st.session_state.user_wins += 1
        st.success("You Win!")
    elif user_pick == "Paper" and comp_pick == "Rock":
        st.session_state.user_wins += 1
        st.success("You Win!")
    elif user_pick == "Scissors" and comp_pick == "Paper":
        st.session_state.user_wins += 1
        st.success("You Win!")
    elif user_pick == comp_pick:
        st.warning("It's a Draw!")
    else:
        st.session_state.comp_wins += 1
        st.error("You Lost!")

st.write(f"You won: {st.session_state.user_wins}")
st.write(f"Computer won: {st.session_state.comp_wins}")
