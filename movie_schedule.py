# Creating the movie schedule
current_movies = {'The Grinch':'11:00am',
                'Rudolph':'01:00pm',
                'Frosty the snowman':'03:00am',
                'Christmas Vacation':'05:00pm'}

# Shwoing the movie schedule
print("Currently we're showing the folling movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtimne for?\n')

# Presenting the showtime
showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)