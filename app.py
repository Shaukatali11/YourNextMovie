import pickle
import streamlit as st
import requests

st.header("Movie Recommendation system using Machine Learning")
movie=pickle.load('C:\ml project\tmbd_500 Movie recommender system\artificates\movie_list.pkl', 'rb')
similarity = pickle.load('artificates/similarity.pkl' , 'rb')

#create a box in which all movie name mension

movie_list=movie['title'].values
st.selectbox