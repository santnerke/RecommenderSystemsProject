from sentence_transformers import SentenceTransformer, util
import torch

def movieDescription_byID(movie_id, movies_df):
    movie = movies_df[movies_df['movieId'] == movie_id]
    if not movie.empty:
        return movie.iloc[0]['description']
    else:
        raise ValueError(f"Movie with ID {movie_id} not found.")

def recommend_movies_by_embedding(movie_id, movies_df, top_k=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    descriptions = movies_df['description'].tolist()
    titles = movies_df['title'].tolist()

    try:
        query = movieDescription_byID(movie_id, movies_df)
    except ValueError as e:
        print(e)
        return []

    embeddings = model.encode(descriptions, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)

    cosine_scores = util.cos_sim(query_embedding, embeddings)[0]

    # Exclude self
    try:
        query_index = descriptions.index(query)
        cosine_scores[query_index] = -1.0
    except ValueError:
        pass

    top_results = torch.topk(cosine_scores, k=top_k)

    # Prepare structured output
    recommendations = []
    for score, idx in zip(top_results[0], top_results[1]):
        recommendations.append({
            'title': titles[idx],
            'similarity': float(score),
            'description': descriptions[idx]
        })

    return recommendations
