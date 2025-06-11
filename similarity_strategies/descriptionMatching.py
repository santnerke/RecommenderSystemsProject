from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_movies_by_description(id, movies):
    descriptions = [movie["description"] for movie in movies]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    similarities = similarity_matrix[id]

    similarities[id] = -1

    top_indices = np.argsort(similarities)[::-1][:5]

    print("By Description\n")
    print("Top 5 similar Movies:\n")
    for rank, i in enumerate(top_indices, 1):
        print(f"{rank}. ({similarities[i]:.2f} Similarity): {descriptions[i]}")
