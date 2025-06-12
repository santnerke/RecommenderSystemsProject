def recommend_movies_by_lead_actors(movie_id, df_movies, top_n=5):

    if movie_id not in df_movies['movieId'].values:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_actors = set(df_movies[df_movies['movieId'] == movie_id]['lead_actors'].values[0])

    similarity_scores = []

    for _, row in df_movies.iterrows():
        # skip reference movie
        if row['movieId'] == movie_id:
            continue

        actors = set(row['lead_actors'])

        # find common actors with the reference movie
        shared = ref_actors.intersection(actors)

        # if shared actors - store id, movie and the shared actors
        if shared:
            similarity_scores.append({
                'movieId': row['movieId'],
                'title': row['title'],
                'shared_actors': list(shared)
            })
    # sort by number of common actors
    results = sorted(similarity_scores, key=lambda x: len(x['shared_actors']), reverse=True)

    return results[:top_n]
