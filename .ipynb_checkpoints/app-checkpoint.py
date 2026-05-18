import streamlit as st
import pickle
import pandas as pd 


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movie_list = movie_list['title'].values


st.title("Recommender System for Movies")

options = st.selectbox(
    "Select a movie you like:",
    (movie_list)
)