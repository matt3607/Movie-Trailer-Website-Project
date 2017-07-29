import fresh_tomatoes 
import media 

#Toy Story
toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=NTdKQzVFeis")
#print (toy_story.storyline)     

#Avatar
avatar = media.Movie ("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")         
#print (avatar.storyline)
#avatar.show_trailer()

#Iron Man
iron_man = media.Movie("Iron Man",
                    "A billionaire industrialist and genius inventor, Tony Stark builds an armored suit",
                    "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ak.jpg",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")         
print (iron_man.storyline)
iron_man.show_trailer()

#Batman Begins
batman_begins = media.Movie ("Batman Begins",
                    "A young Bruce Wayne (Christian Bale) travels to the Far East, where he's trained in the martial arts by Henri Ducard (Liam Neeson), a member of the mysterious League of Shadows. When Ducard reveals the League's true purpose -- the complete destruction of Gotham City -- Wayne returns to Gotham intent on cleaning up the city without resorting to murder. With the help of Alfred (Michael Caine), his loyal butler, and Lucius Fox (Morgan Freeman), a tech expert at Wayne Enterprises, Batman is born.",
                    "http://www.gstatic.com/tv/thumb/movieposters/35903/p35903_p_v8_aw.jpg",
                    "https://www.youtube.com/watch?v=vak9ZLfhGnQ")         
#print (batman_begins.storyline)

#Thor
thor = media.Movie ("Thor",
                    "The epic adventure Thor spans the Marvel Universe from present day Earth to the mystical realm of Asgard. At the center of the story is The Mighty Thor, a powerful but arrogant warrior whose reckless actions reignite an ancient war. As a result, Thor is banished to Earth where he is forced to live among humans. When the most dangerous villain of his world sends its darkest forces to invade Earth, Thor learns what it takes to be a true hero.-- (C) Paramount Pictures",
                    "http://static.rogerebert.com/uploads/movie/movie_poster/thor-2011/large_jqcMUV73jEhO0gv5yi28FD8JbHQ.jpg",
                    "https://www.youtube.com/watch?v=JOddp-nlNvQ")         
#print (thor.storyline)


#Captain America
captain_america = media.Movie ("Captain America",
                    "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                    "https://popculturepug.files.wordpress.com/2015/03/captain-america-the-first-avenger.jpg",
                    "https://www.youtube.com/watch?v=s2Pxe48WsCw")         
#print (captain_america.storyline)

movies = [toy_story, avatar, iron_man, batman_begins, thor, captain_america]
fresh_tomatoes.open_movies_page (movies)

print (media.Movie.VALID_RATINGS)