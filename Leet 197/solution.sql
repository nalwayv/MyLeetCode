-- 197. Rising Temperature
-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
SELECT A.id
FROM Weather AS A
JOIN Weather AS B
    --mysql: ON DATE_SUB(A.recordDate, INTERVAL 1 DAY) = B.recordDate
    ON DATE(A.recordDate, '-1 day') = B.recordDate
    WHERE A.temperature > B.temperature;