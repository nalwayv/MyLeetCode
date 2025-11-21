-- 1050. Actors and Directors Who Cooperated At Least Three Times
--
-- Input: 
-- ActorDirector table:
-- +-------------+-------------+-------------+
-- | actor_id    | director_id | timestamp   |
-- +-------------+-------------+-------------+
-- | 1           | 1           | 0           |
-- | 1           | 1           | 1           |
-- | 1           | 1           | 2           |
-- | 1           | 2           | 3           |
-- | 1           | 2           | 4           |
-- | 2           | 1           | 5           |
-- | 2           | 1           | 6           |
-- +-------------+-------------+-------------+
-- Output: 
-- +-------------+-------------+
-- | actor_id    | director_id |
-- +-------------+-------------+
-- | 1           | 1           |
-- +-------------+-------------+
-- Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(director_id) >= 3