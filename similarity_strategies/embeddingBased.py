from sentence_transformers import SentenceTransformer, util
import torch
from .database import filmDescripiton_byID

def recommend_movies_by_embedding(movies, id):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    descriptions = [movie["beschreibung"] for movie in movies]
    query = filmDescripiton_byID(id)

    embeddings = model.encode(descriptions, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)

    cosine_scores = util.cos_sim(query_embedding, embeddings)[0]

    # Index der Query-Beschreibung in der Liste finden
    if query in descriptions:
        query_index = descriptions.index(query)
        cosine_scores[query_index] = -1.0  # Score auf sehr niedrig setzen

    top_results = torch.topk(cosine_scores, k=5)

    print("\nQuery:", query)
    print("Top matches:")

    for score, idx in zip(top_results[0], top_results[1]):
        print(f"{score:.2f} – {descriptions[idx]}")
