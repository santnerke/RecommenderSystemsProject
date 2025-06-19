def recommend_movies_by_lead_actors(movie_id, movie_list, top_n=5):
    # Find reference movie
    ref_movie = next((m for m in movie_list if m.get('id') == movie_id), None)
    if not ref_movie:
        raise ValueError(f"Movie ID {movie_id} not found.")

    # Extract lead actors (first three from 'actors' list)
    ref_actors = ref_movie.get('actors') or []
    ref_lead_actors = set(ref_actors[:3])  # first three actors as lead actors

    similarity_scores = []

    for movie in movie_list:
        if movie.get('id') == movie_id:
            continue

        actors = movie.get('actors') or []
        lead_actors = set(actors[:3])
        print(lead_actors)

        shared = ref_lead_actors.intersection(lead_actors)

        if shared:
            similarity_scores.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'shared_actors': list(shared)
            })

    results = sorted(similarity_scores, key=lambda x: len(x['shared_actors']), reverse=True)
    return results[:top_n]
