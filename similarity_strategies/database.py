import csv
import json
import os

json_folder = "./extracted_content_ml-latest"
moviedata = "./ml-latest-small/movies.csv"

def filmDescripiton_byID(film_id):
    pfad = os.path.join(json_folder, f"{film_id}.json")
    try:
        with open(pfad, "r", encoding="utf-8") as f:
            daten = json.load(f)
            description = (
                daten.get("movielens", {}).get("plotSummary") or
                "No description found"
            )
            return description
    except FileNotFoundError:
        return "Datei nicht gefunden."
    except json.JSONDecodeError:
        return "Ungültiges JSON-Format."

def lade_alle_beschreibungen():
    daten = []
    with open(moviedata, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for zeile in reader:
            if len(zeile) < 2:
                continue
            film_id = zeile[0].strip()
            titel = zeile[1].strip()
            genres = zeile[2].strip() if len(zeile) > 2 else ""
            beschreibung = filmDescripiton_byID(film_id)
            daten.append({
                "id": film_id,
                "titel": titel,
                "genres": genres,
                "beschreibung": beschreibung
            })
    return daten
