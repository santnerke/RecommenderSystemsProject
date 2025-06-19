# movies/management/commands/import_movielens.py

from django.core.management.base import BaseCommand
from rs_app.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Import MovieLens 1M dataset with extended JSON filter'

    def add_arguments(self, parser):
        parser.add_argument('data_path', type=str)

    def handle(self, *args, **options):
        path = options['data_path']

        self.stdout.write("Importing movies from JSON files...")

        json_files = [
            filename for filename in os.listdir(path) if filename.endswith('.json')
        ]

        for filename in json_files:
            movie_id = filename.split('.')[0]
            json_file = os.path.join(path, filename)

            with open(json_file, encoding='utf-8') as jf:
                data = json.load(jf)
                movielens = data.get("movielens", {})

                Movie.objects.update_or_create(
                    id=movie_id,
                    defaults={
                        'title': movielens.get("title"),
                        'genres': movielens.get("genres", ""),  # fallback if needed
                        'release_year': movielens.get("releaseYear"),
                        'actors': movielens.get("actors"),
                        'plot_summary': movielens.get("plotSummary"),
                        'duration': movielens.get("runtime"),
                        'backdrop_path': (
                            f"https://image.tmdb.org/t/p/original{movielens['backdrop_path']}"
                            if movielens.get("backdrop_path") else None
                        )
                    }
                )

        self.stdout.write(self.style.SUCCESS("All movies imported from JSON files."))