import fresh_tomatoes
import media

salt=media.Movie("Salt", "When Evelyn Salt (Angelina Jolie) became a CIA officer, she swore an oath to duty, honor and country. But, when a defector accuses her of being a Russian spy, Salt's oath is put to the test.",
                      "http://static.rogerebert.com/uploads/movie/movie_poster/salt-2010/large_nSYf9926SJlIZ7DIkiKL8NxaWZ4.jpg",
                      "https://www.youtube.com/watch?v=QZ40WlshNwU")


civil_war=media.Movie("Civil War",
					"Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage.",
					"http://img.wallpaperfolder.com/f/7AFC52A3795A/marvel-civil-war-resolution-fmmrf.jpg",
					"https://www.youtube.com/watch?v=gce5cli0VB4")


terminator=media.Movie("Terminator",
						"Disguised as a human, a cyborg assassin known as a Terminator (Arnold Schwarzenegger) travels from 2029 to 1984 to kill Sarah Connor (Linda Hamilton). Sent to protect Sarah is Kyle Reese (Michael Biehn), who divulges the coming of Skynet, an artificial intelligence system that will spark a nuclear holocaust. Sarah is targeted because Skynet knows that her unborn son will lead the fight against them. With the virtually unstoppable Terminator in hot pursuit, she and Kyle attempt to escape.",
						"http://t1.gstatic.com/images?q=tbn:ANd9GcRHzSaUCOKu1RwS-bfbaUeeo_I1JcBkiuJRjBElvJi7qsHXkUkJ",
						"https://www.youtube.com/watch?v=62E4FJTwSuc")

ice_ages=media.Movie("Ice Ages",
						"Twenty-thousand years ago, Earth is a wondrous, prehistoric world filled with great danger, not the least of which is the beginning of the Ice Age.",
						"http://www.richardcrouse.ca//wp-content/uploads/2013/09/Ice-age-3-10.jpg",
						"https://www.youtube.com/watch?v=HyLquKn3Swc")

deep_water=media.Movie("Deepwater",
						"the Deepwater Horizon drilling rig explodes in the Gulf of Mexico, igniting a massive fireball that kills several crew members.",
						"http://www.deepwaterhorizon.movie/assets/images/dwhepkSocial.jpg",
						"https://www.youtube.com/watch?v=8yASbM8M2vg")
sully=media.Movie("Sully",
					"Chesley Sully Sullenberger (Tom Hanks) tries to make an emergency landing in New York's Hudson River after US Airways Flight 1549 strikes a flock of geese.",
					"http://www.sullysullenberger.com/wp-content/uploads/2016/06/sully-poster-sized.jpg",
					"https://www.youtube.com/watch?v=mjKEXxO2KNE")
movies=[salt,civil_war,terminator,ice_ages,deep_water,sully]
fresh_tomatoes.open_movies_page(movies)
