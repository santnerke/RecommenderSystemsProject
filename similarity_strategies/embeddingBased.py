from sentence_transformers import SentenceTransformer, util
import torch

def movieDescription_byID(movie_id, movies_list):
    # Find the movie with the given ID in a list of dictionaries
    for movie in movies_list:
        if movie.get('id') == movie_id:  # or 'movieId' if your dicts use that
            return movie.get('plot_summary') or ""
    else:
        raise ValueError(f"Movie with ID {movie_id} not found.")

def recommend_movies_by_embedding(movie_id, movies_list, top_k=5):
    # Load sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Extract all descriptions, titles, and ids from list
    descriptions = [m.get('plot_summary') or '' for m in movies_list]
    titles = [m.get('title') or '' for m in movies_list]
    ids = [m.get('id') for m in movies_list]

    try:
        # Get description for the given movie_id
        query = movieDescription_byID(movie_id, movies_list)
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

    # Build recommendations list with title, similarity score, description, and id
    recommendations = []
    for score, idx in zip(top_results[0], top_results[1]):
        recommendations.append({
            'id': ids[idx],  # added id here
            'title': titles[idx],
            'similarity': float(score),
            'description': descriptions[idx]
        })

    return recommendations