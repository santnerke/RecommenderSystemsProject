from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_movies_by_description(movies, id):
    descriptions = [movie["beschreibung"] for movie in movies]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    similarities = similarity_matrix[id]

    similarities[id] = -1

    top_indices = np.argsort(similarities)[::-1][:5]

    print(f"\nOriginalbeschreibung:\n{descriptions[id]}\n")
    print("Top 5 ähnliche Filme:\n")
    for rank, i in enumerate(top_indices, 1):
        print(f"{rank}. ({similarities[i]:.2f} Ähnlichkeit): {descriptions[i]}")
