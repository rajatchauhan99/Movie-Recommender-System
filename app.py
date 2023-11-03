import streamlit as st

import pickle

movies_df = pickle.load(open("movies.pkl", "rb"))
similarity_score_matrix = pickle.load(open("similarity_score_matrix.pkl", "rb"))

def recommend(movie):
    movie_index = movies_df[movies_df["title"] == movie].index[0]
    distances = similarity_score_matrix[movie_index]
    top_5_movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in top_5_movies_list:
        movie_id = i[0]
        # fetching movie poster through API

        recommended_movies.append(movies_df["title"][i[0]])
    return recommended_movies


movies_title = movies_df["title"].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select Movie" ,movies_title)

if st.button("Recommend"):
    recommended_movies = recommend(selected_movie_name)
    for i in recommended_movies:
        st.write(i)
