## Background

Rihal Cinema is trying to build a movie rating system and website. They are trying to establish a competitive edge in the market by focusing on user experience, accurate ratings, and personalized recommendations. The system should cater to a diverse audience of movie enthusiasts, offering a wide range of movie genres.

## Problem statement

Your task is to develop a backend server system (API) for a movie rating platform. The platform allows registered users to rate movies and view average ratings. The system should provide a seamless experience for users to rate movies, while ensuring data integrity, security, and scalability.

## Overall Requirements and APIs

Abdul Karim is a movie enthusiast and an employee of Rihal Cinema. He has provided you with what he wants you to achieve:

1.  I want to register a user into the system.

2.  I want all API’s (except the user registration API) to be protected using Basic Authentication

3.  I will provide you with a JSON file containing a list of movies in my cinema. The list will contain the name and description of each movie. I want you to add these movies to your database when your applications start up. However, there are some missing pieces of information namely: release date, main cast, director, and budget. This information is hosted at: [https://cinema.stag.rihal.tech](https://cinema.stag.rihal.tech), where the API endpoint is: `GET /api/movie/{movie_id}`

4.  I want to be able to rate a movie from 1 to 10, step of 1.

5.  I want an API to return to me the list of all movies in the database. This should return the ID, name, description and average rating (average rating of all users in the system) of each movie. The description should be 100 characters or less. If the description exceeds the max limit of 100 characters truncate with “...” however, the last word must be a full meaningful word. For example, not accepted: “this movie is beauti...”, accepted: “this movie is ...”

6.  I want an API to return detailed information about a specific movie given the ID. This API should return the following: id, name, description, release date, main cast, director, budget, budget in English words (i.e. Budget 1.5B to one billion five hundred million), my rating and the average rating (average rating of all users in the system)

7.  I want to be able to search for a movie. This API should be able to return a list of movies (id, name, description) based on a search parameter which matches either the name or description.

8.  I want an API that returns my top 5 rated movies (id, name, rating) in descending order (ordered by the rating)

9.  I would like a feature called 'Memories' where I can record personal memories related to a movie. These memories would include a title, date, photos and a story. For instance, I would like to include the photos I took the day I watched 'Mad Max' in theaters, along with the date and the story of what my friends and I did that day.

10. I want an API to return all my memories (id, movie id, movie name, title).

11. I want an API to return a memory (id, movie id, movie name, title, story, time ordered list of photos (id, photo name, photo extension i.e. PNG, size i.e. 3KB, time created)) given its id.

12. I want an API that returns the memory photo given its id.

13. I want an API to update a memory. This includes changing the title or/and the story

14. I want an API to upload more photos to a memory or delete some.

15. I want an API to delete a memory.

16. I want an API that calculates the top 5 used words in all stories in memories across the system. This should ignore stop words (e.g. “and”, “the”, “to” etc...)

17. I want an API that extract any links or URLs mentioned in a story given the memory ID

18. For fun, I would like to add a puzzle where the user enters a scrambled movie name and the system tries to guess the actual movie. Say I enter: “eund”, the system should be able to return a movie (id, name, description) -> e.g. (12 or uuid, “Dune”, “A noble family becomes embroiled in a war for control over the galaxy's most valuable asset while its heir becomes troubled by visions of a dark future.”). Another example: “askldjfhaksdf” the API should return “404 not found”

19. To compare my ratings to the average, return a list of the maximum. Say I have ratings of [{“Dune”, 10}, {“The Hobbit”, 5}, {“The Godfather”, 7}] and the corresponding average ratings [{“Dune”, 7}, {“The Hobbit”, 9}, {“The Godfather”, 10}]. This API should return [{id, “Dune”, 10, true}, {id, “The Hobbit”, 9, false}, {id, “The Godfather”, 10, false}] as you can see, the returned list only includes the maximum ratings in addition to the fact if it was my rating (true) or not (false)

## Technical Requirements:

1. Use [git](https://git-scm.com/) as your version control system.

2. Your code MUST be on github. Your submission should include the link to the repository.

3. Use whatever language and framework you desire.

4. Database: You are required to use [PostgreSQL](https://www.postgresql.org/). You can use [ElephantSQL](https://www.elephantsql.com/) (FREE) or the [docker instance](https://hub.docker.com/_/postgres) if you decided to dockerize your project (check extra credit below).

5. File Storage: You can use any storage you want (e.g., [MinIO](https://min.io/), [Google Cloud Storage](https://cloud.google.com/storage))

## Extra Credit

You are not required to complete these tasks, but doing so will increase your chances of winning the competition and provide an opportunity to showcase your capabilities. You can do them all or some.

1.  Dockerize your project using [docker](https://www.docker.com/) and docker compose to run your project.

2.  Imagine a star system where users can purchase stars to award to movies as a gesture of excellence and appreciation. Construct an API where the user can get the minimum number of stars to award given movies (API should expect a list of movie IDs). Put the ratings in an ordered list (exact order given by the user), stars will be given to these movies based on the following requirements:

    - Each movie must have at least one star.
    - Movies with higher ratings get more stars than their neighbours.

    Return the minimum number of stars the user needs to have to distribute the stars to the moivies.

    For example:

    - Movie ratings = [2,1,2] should return 5.

    - Movie ratings = [10,1,2,8,7,3] should return 11.

3.  Implement a chat room feature that allows users to discuss individual movies. Each chat room will be dedicated to a specific movie, facilitating connections for multiple users. Utilize websockets to enable seamless communication within these chat rooms.

## NOTE

1. This is a purely backend challenge! You should only create an API server without any front-end component.

---

# Unleash Your Creativity - Enjoy!
