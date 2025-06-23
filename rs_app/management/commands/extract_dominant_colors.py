from django.core.management.base import BaseCommand
from colorthief import ColorThief
import os, json
from rs_app.models import Movie  # adjust if your model name is different
from django.conf import settings


class Command(BaseCommand):
    help = 'Extract dominant colors from movie posters and save to JSON'

    def handle(self, *args, **kwargs):
        poster_dir = os.path.join(settings.BASE_DIR, 'rs_app', 'static', 'movie_posters')
        output_file = os.path.join(settings.BASE_DIR, 'dominant_colors.json')

        movie_list = Movie.objects.all()  # adjust if needed

        color_map = {}
        for movie in movie_list:
            poster_path = os.path.join(poster_dir, f"{movie.id}.jpg")
            if not os.path.exists(poster_path):
                continue
            try:
                color_thief = ColorThief(poster_path)
                color = color_thief.get_color(quality=1)
                color_map[str(movie.id)] = color
                self.stdout.write(self.style.SUCCESS(f"✓ {movie.title} → {color}"))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"✗ Failed for {movie.title}: {e}"))

        with open(output_file, 'w') as f:
            json.dump(color_map, f)

        self.stdout.write(self.style.SUCCESS(f"\nDone! Colors saved to {output_file}"))
