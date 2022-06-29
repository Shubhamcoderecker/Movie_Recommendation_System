import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_lst[movies_lst["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_rec = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_rec:
        recommended_movies.append(movies_lst.iloc[i[0]].title)
    return recommended_movies

movies_lst = pickle.load(open("movies.pkl", "rb"))
movies_list = movies_lst["title"].values

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select the Movie", movies_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
