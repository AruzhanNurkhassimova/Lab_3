movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1
def above(movie):
    return movie["imdb"]>5.5

print(above(movies[0]))
#2


def sublist(movies):
    result = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            result.append(movie)
    return result

print(sublist(movies))


#3
def by_category(movies, category):
    result = []
    for movie in movies:
        if movie["category"] == category:
            result.append(movie)
    return result

print(by_category(movies, "Crime"))


#4
def average_imdb(movies):
    if not movies:
        return 0
    total_imdb = 0
    for movie in movies:
        total_imdb += movie["imdb"]
    return total_imdb / len(movies)
    
print(average_imdb(movies))


#5
def average_imdb_by_category(movies, category):
    category_movies = by_category(movies, category)
    return average_imdb(category_movies)
    
print(average_imdb_by_category(movies, "Romance"))