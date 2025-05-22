import streamlit as st
from preprocess import clean_text, preprocess_text, get_similarity_matrix, get_recommendations

@st.cache_data
def load_data():
    return pd.read_csv('scrapped_2024.csv')

@st.cache_data
def load_similarity(df):
    df['cleaned_story'] = df['Storyline'].apply(clean_text).apply(preprocess_text)
    return get_similarity_matrix(df)

def main():
    st.title('Movie Recommendation System')
    st.write('Find similar movies based on storyline similarity')

    try:
        df = load_data()
        if not all(col in df.columns for col in ['Movie_Name', 'Storyline']):
            st.error("CSV file must contain 'Movie_Name' and 'Storyline' columns")
            return
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return

    similarity_matrix = load_similarity(df)

    option = st.radio("Choose input method:", ('Select from existing movies', 'Enter custom storyline'))

    if option == 'Select from existing movies':
        movie_name = st.selectbox('Select a movie:', df['Movie_Name'].tolist())

        if st.button('Get Recommendations'):
            recommendations = get_recommendations(movie_name, df, similarity_matrix)
            if recommendations.empty:
                st.write("No recommendations found.")
            else:
                st.subheader(f"Top 5 movies similar to '{movie_name}':")
                for _, row in recommendations.iterrows():
                    st.write(f"**{row['Movie_Name']}**")
                    st.write(row['Storyline'])
                    st.write("---")

    else:
        user_input = st.text_area('Enter a movie storyline:')

        if st.button('Find Similar Movies'):
            if not user_input.strip():
                st.warning('Please enter a storyline')
            else:
                cleaned_input = preprocess_text(clean_text(user_input))
                temp_df = df.copy()
                temp_df.loc[len(temp_df)] = ['User Input', user_input, cleaned_input]

                vectorizer = TfidfVectorizer()
                tfidf_matrix = vectorizer.fit_transform(temp_df['cleaned_story'])
                sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

                input_idx = len(temp_df) - 1
                sim_scores = list(enumerate(sim_matrix[input_idx]))
                sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
                movie_indices = [i[0] for i in sim_scores]

                st.subheader("Top 5 recommended movies:")
                for idx in movie_indices:
                    st.write(f"**{temp_df.iloc[idx]['Movie_Name']}**")
                    st.write(temp_df.iloc[idx]['Storyline'])
                    st.write("---")

if __name__ == '__main__':
    main()
