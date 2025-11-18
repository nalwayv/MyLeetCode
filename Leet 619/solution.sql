-- 619. Biggest Single Number
--
-- Input: 
-- MyNumbers table:
-- +-----+
-- | num |
-- +-----+
-- | 8   |
-- | 8   |
-- | 3   |
-- | 3   |
-- | 1   |
-- | 4   |
-- | 5   |
-- | 6   |
-- +-----+
--
-- Output: 
-- +-----+
-- | num |
-- +-----+
-- | 6   |
-- +-----+

SELECT max(num) as num
FROM
(
	SELECT num 
	FROM MyNumbers 
	GROUP by num HAVING count(num) = 1
) as numbers