-- 1667. Fix Names in a Table
--
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | user_id        | int     |
-- | name           | varchar |
-- +----------------+---------+
--
-- Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
-- Return the result table ordered by user_id.
-- The result format is in the following example.

select user_id, concat(substr(upper(name), 1, 1), substr(lower(name), 2)) as name
from Users
order by user_id