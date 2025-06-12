from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from similarity_strategies.genreMatching import recommend_movies_by_genre
from similarity_strategies.leadActorsBased import recommend_movies_by_lead_actors
from similarity_strategies.descriptionMatching import recommend_movies_by_description
from similarity_strategies.embeddingBased import recommend_movies_by_embedding
import pandas as pd

def index(request):
    return render(request, 'rs_app/index.html')

def recommend(request):
    movie_id = int(request.GET.get('movie_id'))
    genre_recs = recommend_movies_by_genre(movie_id, df_movies)
    actor_recs = recommend_movies_by_lead_actors(movie_id, df_movies)
    desc_recs = recommend_movies_by_description(movie_id, df_movies)
    embe_recs = recommend_movies_by_embedding(movie_id, df_movies)

    return render(request, 'rs_app/recommend.html', {
        'genre_recommendations': genre_recs,
        'actor_recommendations': actor_recs,
        'description_recommendations': desc_recs,
        'embedding_recommendations': embe_recs,
        'movie_id': movie_id,
    })

# test data
import pandas as pd

df_movies = pd.DataFrame([
    {
        'movieId': 1,
        'title': 'Toy Story (1995)',
        'genres': 'Adventure|Animation|Children|Comedy|Fantasy',
        'lead_actors': ['Tom Hanks', 'Tim Allen'],
        'description': 'When young Andy leaves his room, his toys spring to life and embark on an epic journey. Woody, a cowboy doll, feels threatened by the arrival of Buzz Lightyear, a flashy new space ranger. As jealousy turns into friendship, the two must work together to reunite with Andy before it’s too late.'
    },
    {
        'movieId': 2,
        'title': 'Jumanji (1995)',
        'genres': 'Adventure|Children|Fantasy',
        'lead_actors': ['Robin Williams', 'Tim Allen'],
        'description': 'After discovering a mysterious board game, two children accidentally release a man who has been trapped inside it for decades. As they continue playing, wild jungle creatures invade their town, and they must finish the game to restore order and send the magic back where it came from.'
    },
    {
        'movieId': 356,
        'title': 'Forrest Gump (1994)',
        'genres': 'Comedy|Drama|Romance|War',
        'lead_actors': ['Tom Hanks', 'Robin Wright'],
        'description': 'Forrest Gump, a kind-hearted but simple man from Alabama, inadvertently becomes part of major historical events in America. With unwavering love for his childhood friend Jenny, Forrest shares his life story — filled with humor, heartbreak, and unexpected triumphs — from a bench in Savannah.'
    },
    {
        'movieId': 4022,
        'title': 'Cast Away (2000)',
        'genres': 'Drama',
        'lead_actors': ['Tom Hanks', 'Helen Hunt'],
        'description': 'Chuck Noland, a FedEx systems engineer, is stranded on a deserted island after a plane crash. Isolated from the world, he must learn how to survive against the odds, confronting his fears, loneliness, and the ultimate challenge of returning to a life that has moved on without him.'
    },
    {
        'movieId': 3,
        'title': 'Grumpier Old Men (1995)',
        'genres': 'Comedy|Romance',
        'lead_actors': ['Walter Matthau', 'Jack Lemmon'],
        'description': 'Retired neighbors Max and John are back with their lovable bickering and rivalry. When a spirited woman opens a new restaurant in town, the men’s friendship is tested once again as romance stirs between them and the women in their lives. A heartfelt, humorous tale about love later in life.'
    },
    {
        'movieId': 9999999999,
        'title': 'Test with Tom Hanks & Tim Allen',
        'genres': 'Documentary',
        'lead_actors': ['Tom Hanks', 'Tim Allen'],
        'description': 'This behind-the-scenes documentary delves into the enduring partnership of Tom Hanks and Tim Allen, exploring their iconic roles in animation and live-action cinema, their creative process, and their lasting impact on Hollywood storytelling.'
    },
    {
        'movieId': 99999999999,
        'title': 'Test with the same genres',
        'genres': 'Adventure|Animation|Children|Comedy|Fantasy',
        'lead_actors': ['xy'],
        'description': 'In a magical realm where dreams blend with reality, a young adventurer sets out on a quest to save their kingdom from a spreading darkness. Along the way, they befriend eccentric creatures, face whimsical challenges, and discover the power of courage, laughter, and imagination.'
    },
    {
        'movieId': 11,
        'title': 'The Lion King (1994)',
        'genres': 'Animation|Adventure|Drama|Musical|Children',
        'lead_actors': ['Matthew Broderick', 'James Earl Jones'],
        'description': 'Young lion prince Simba flees his kingdom after the tragic death of his father Mufasa. Growing up in exile, he wrestles with guilt and destiny. With help from new friends, Simba must return to reclaim his throne and save the Pride Lands from tyranny.'
    },
    {
        'movieId': 12,
        'title': 'The Shawshank Redemption (1994)',
        'genres': 'Drama|Crime',
        'lead_actors': ['Tim Robbins', 'Morgan Freeman'],
        'description': 'Wrongfully convicted banker Andy Dufresne forms an unlikely friendship with fellow inmate Red. Over decades in Shawshank Prison, Andy retains hope, using his intelligence to uplift others—and plan an ingenious escape that will change everything.'
    },
    {
        'movieId': 13,
        'title': 'Inception (2010)',
        'genres': 'Action|Adventure|Sci-Fi|Thriller',
        'lead_actors': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt'],
        'description': 'A skilled thief enters people’s dreams to steal secrets. When offered a chance to erase his criminal record, he must instead plant an idea in a target’s mind—an “inception”—while navigating shifting dreamscapes and inner demons.'
    },
    {
        'movieId': 14,
        'title': 'The Grand Budapest Hotel (2014)',
        'genres': 'Comedy|Drama|Adventure',
        'lead_actors': ['Ralph Fiennes', 'Tony Revolori'],
        'description': 'The legendary concierge Gustave H. and lobby boy Zero become unlikely partners in a madcap adventure involving a stolen Renaissance painting, a family inheritance feud—and the looming threat of war in 1930s Europe.'
    },
    {
        'movieId': 15,
        'title': 'La La Land (2016)',
        'genres': 'Romance|Drama|Musical',
        'lead_actors': ['Ryan Gosling', 'Emma Stone'],
        'description': 'Aspiring actress Mia and jazz musician Sebastian fall in love while chasing their dreams in Los Angeles. As their artistic ambitions rise, so do the challenges of balancing romance, career, and sacrifice.'
    }
])
