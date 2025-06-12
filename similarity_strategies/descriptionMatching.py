from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_movies_by_description(movie_id, movies_df, top_k=5):
    descriptions = movies_df['description'].tolist()
    titles = movies_df['title'].tolist()

    try:
        query_index = movies_df[movies_df['movieId'] == movie_id].index[0]
    except IndexError:
        print(f"Movie ID {movie_id} not found.")
        return []

    # TF-IDF encoding
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(tfidf_matrix)
    similarities = similarity_matrix[query_index]
    similarities[query_index] = -1  # Exclude self

    top_indices = np.argsort(similarities)[::-1][:top_k]

    recommendations = []
    for idx in top_indices:
        recommendations.append({
            'title': titles[idx],
            'similarity': float(similarities[idx]),
            'description': descriptions[idx]
        })

    return recommendations