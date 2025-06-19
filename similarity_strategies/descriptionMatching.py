from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_movies_by_description(movie_id, movies_list, top_k=5):
    # Get all descriptions and titles from dataframe
    descriptions = [m.get('plot_summary') or '' for m in movies_list]
    titles = [m.get('title') or '' for m in movies_list]
    ids = [m.get('id') for m in movies_list]

    try:
        # Find index of the movie with the given ID
        query_index = ids.index(movie_id)
    except ValueError:
        print(f"Movie ID {movie_id} not found.")
        return []

    # Convert descriptions to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    # Compute cosine similarity matrix between all movies
    similarity_matrix = cosine_similarity(tfidf_matrix)
    # Get similarity scores for the query movie
    similarities = similarity_matrix[query_index]
    # Exclude the query movie itself from recommendations
    similarities[query_index] = -1

    # Get indices of top-k most similar movies
    top_indices = np.argsort(similarities)[::-1][:top_k]

    # Build list of recommended movies with title, similarity, and description
    recommendations = []
    for idx in top_indices:
        recommendations.append({
            'title': titles[idx],
            'similarity': float(similarities[idx]),
            'description': descriptions[idx]
        })

    return recommendations