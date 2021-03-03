-- lists all SHOWs contained in hbtn_0d_tvSHOWs that have at least one genre linked
-- Each record should display: tv_SHOWs.title - tv_SHOW_genres.genre_id
-- Results must be sorted in ascending ORDER BY tv_SHOWs.title and tv_SHOW_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
