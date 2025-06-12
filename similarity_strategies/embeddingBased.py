from sentence_transformers import SentenceTransformer, util
import torch

def movieDescription_byID(movie_id, movies_df):
    # Get the description of the movie by its ID
    movie = movies_df[movies_df['movieId'] == movie_id]
    if not movie.empty:
        return movie.iloc[0]['description']
    else:
        raise ValueError(f"Movie with ID {movie_id} not found.")

def recommend_movies_by_embedding(movie_id, movies_df, top_k=5):
    # Load sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Extract all descriptions and titles from dataframe
    descriptions = movies_df['description'].tolist()
    titles = movies_df['title'].tolist()

    try:
        # Get description for the given movie_id
        query = movieDescription_byID(movie_id, movies_df)
    except ValueError as e:
        print(e)
        return []

    # Encode all movie descriptions to embeddings
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    # Encode query description to embedding
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Compute cosine similarity scores between query and all movies
    cosine_scores = util.cos_sim(query_embedding, embeddings)[0]

    # Set similarity of the query movie to -1 to exclude it from results
    try:
        query_index = descriptions.index(query)
        cosine_scores[query_index] = -1.0
    except ValueError:
        pass

    # Get top-k movies with highest similarity scores
    top_results = torch.topk(cosine_scores, k=top_k)

    # Build recommendations list with title, similarity score, and description
    recommendations = []
    for score, idx in zip(top_results[0], top_results[1]):
        recommendations.append({
            'title': titles[idx],
            'similarity': float(score),
            'description': descriptions[idx]
        })

    return recommendations