import os
import django
from django.core.management import call_command

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rs_project.settings')
django.setup()

# Run management commands
#call_command('makemigrations')
#call_command('migrate')
call_command('import_movielens', 'data/movie_information')
call_command('runserver')