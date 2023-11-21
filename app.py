import streamlit as st
import numpy as np

N = 
p = 

flips = np.random.random(N)

nb_heads = np.sum(np.where(flips < p, 1, 0))
nb_tails = N - nb_heads

percentage_heads = np.round(100*nb_heads/N, 2)
percentage_tails = np.round(100*nb_tails/N, 2) 

