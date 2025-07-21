-- LeetCode: 1341. Movie Rating
-- Full script for PostgreSQL to test the solution

-- 1. Drop tables if they exist
DROP TABLE IF EXISTS MovieRating;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Users;

-- 2. Create tables
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100)
);

CREATE TABLE MovieRating (
    movie_id INT,
    user_id INT,
    rating INT,
    created_at DATE,
    PRIMARY KEY (movie_id, user_id)
);

-- 3. Insert sample data
INSERT INTO Users (user_id, name) VALUES
(1, 'Daniel'),
(2, 'Monica'),
(3, 'Maria'),
(4, 'James');

INSERT INTO Movies (movie_id, title) VALUES
(1, 'Avengers'),
(2, 'Frozen 2'),
(3, 'Joker');

INSERT INTO MovieRating (movie_id, user_id, rating, created_at) VALUES
(1, 1, 3, '2020-01-12'),
(1, 2, 4, '2020-02-11'),
(1, 3, 2, '2020-02-12'),
(1, 4, 1, '2020-01-01'),
(2, 1, 5, '2020-02-17'),
(2, 2, 2, '2020-02-01'),
(2, 3, 2, '2020-03-01'),
(3, 1, 3, '2020-02-22'),
(3, 2, 4, '2020-02-25');

-- 4. Solution query: find the user who rated the most movies (lex order tie-break)
-- and the movie with the highest average rating in February 2020 (lex order tie-break)
WITH UserRatingCount AS (
    SELECT u.name, COUNT(*) AS rating_count
    FROM Users u
    JOIN MovieRating r ON u.user_id = r.user_id
    GROUP BY u.user_id, u.name
),
TopUser AS (
    SELECT name
    FROM UserRatingCount
    WHERE rating_count = (
        SELECT MAX(rating_count) FROM UserRatingCount
    )
    ORDER BY name
    LIMIT 1
),
FebMoviesAvgRating AS (
    SELECT m.title, AVG(r.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating r ON m.movie_id = r.movie_id
    WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
),
TopMovie AS (
    SELECT title
    FROM FebMoviesAvgRating
    WHERE avg_rating = (
        SELECT MAX(avg_rating) FROM FebMoviesAvgRating
    )
    ORDER BY title
    LIMIT 1
)

SELECT name AS results FROM TopUser
UNION ALL
SELECT title FROM TopMovie;
