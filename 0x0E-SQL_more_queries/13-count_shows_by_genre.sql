-- A script that lists all genres from hbtn_0d_tvshows and displays the number
-- First column must be called genre
-- Second column must be called number_of_shows:wq

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
