# https://coinflip-xv7vbpgqbrbskm3niqyurg.streamlit.app/
import numpy as np
import streamlit as st

st.title("Coin flip simulator")
    
# User input for N (integer)
N = st.number_input("Select the number of flips", min_value=1, max_value=1000000, step=1)
    
# User input for p (float)
p = st.number_input("Select the probability of heads", min_value=0.0, max_value=1.0, step=0.01)
    
# Display the selected values
st.write("Selected N:", n)
st.write("Selected p:", p)


flips = np.random.random(N)

nb_heads = np.sum(np.where(flips < p, 1, 0))
nb_tails = N - nb_heads
st.write("Number of heads:", nb_heads)
st.write("Number of tails:", nb_tails)

percentage_heads = np.round(100*nb_heads/N, 2)
percentage_tails = np.round(100*nb_tails/N, 2) 
st.write("Percentage of heads:", percentage_heads)
st.write("Percentage of tails:", percentage_tails)
