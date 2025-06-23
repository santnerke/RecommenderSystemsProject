import json
import numpy as np

with open("dominant_colors.json") as f:
    cached_colors = json.load(f)

def recommend_by_poster_color(selected_movie_id, movie_list, top_n=5):
    selected_color = cached_colors.get(str(selected_movie_id))
    if not selected_color:
        raise ValueError(f"No color data for movie_id {selected_movie_id}")

    recommendations = []
    for movie in movie_list:
        mid = str(movie["id"])
        if mid == str(selected_movie_id) or mid not in cached_colors:
            continue
        recommendations.append({
            "id": movie["id"],
            "title": movie["title"],
            "color": cached_colors[mid]
        })

    def color_distance(c1, c2):
        return np.linalg.norm(np.array(c1) - np.array(c2))

    sorted_recommendations = sorted(
        recommendations,
        key=lambda m: color_distance(selected_color, m["color"])
    )

    return [{"id": m["id"], "title": m["title"]} for m in sorted_recommendations[:top_n]]
