-- 610. Triangle Judgement
--
-- Input: 
-- Triangle table:
-- +----+----+----+
-- | x  | y  | z  |
-- +----+----+----+
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |
-- +----+----+----+
--
-- Output: 
-- +----+----+----+----------+
-- | x  | y  | z  | triangle |
-- +----+----+----+----------+
-- | 13 | 15 | 30 | No       |
-- | 10 | 20 | 15 | Yes      |
-- +----+----+----+----------+

SELECT x, y, z,
	CASE
		WHEN 
			x + y > z AND
			z + x > y AND
			z + y > x 
		THEN 'Yes' ELSE 'No'
	END triangle
FROM Triangle