import streamlit as st
import numpy as np



def main():
    st.title("User Input Demo")
    
    # User input for N (integer)
    n = st.number_input("Select an integer value for N", min_value=1, max_value=1000000, step=1)
    
    # User input for p (float)
    p = st.number_input("Select a float value for p", min_value=0.0, max_value=1.0, step=0.05)
    
    # Display the selected values
    st.write("Selected N:", n)
    st.write("Selected p:", p)

if __name__ == "__main__":
    main()

flips = np.random.random(N)

nb_heads = np.sum(np.where(flips < p, 1, 0))
nb_tails = N - nb_heads

percentage_heads = np.round(100*nb_heads/N, 2)
percentage_tails = np.round(100*nb_tails/N, 2) 

