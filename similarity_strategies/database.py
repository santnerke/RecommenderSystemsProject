import csv
import json
import os

json_folder = "./extracted_content_ml-latest"
moviedata = "./ml-latest-small/movies.csv"

def load_movies():
    data = []
    with open(moviedata, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) < 2:
                continue
            movie_id = line[0].strip()
            title = line[1].strip()
            genre = line[2].strip() if len(line) > 2 else ""
            description = movieDescripiton_byID(movie_id)
            actor = movieActor_byID(movie_id)
            daten.append({
                "id": movie_id,
                "title": title,
                "genre": genre,
                "description": description,
                "actor": actor
            })
    return data

def movieDescripiton_byID(movie_id):
    path = os.path.join(json_folder, f"{movie_id}.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            description = (
                data.get("movielens", {}).get("plotSummary") or
                "No description found"
            )
            return description
    except FileNotFoundError:
        return "Data not found."
    except json.JSONDecodeError:
        return "no JSON-Format."

def movieActor_byID(movie_id):
    path = os.path.join(json_folder, f"{movie_id}.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            description = (
                data.get("movielens", {}).get("") or
                "No description found"
            )
            return description
    except FileNotFoundError:
        return "Data not found."
    except json.JSONDecodeError:
        return "no JSON-Format."
