-- 1179. Reformat Department Table
-- Input:
-- Department table:
-- +------+---------+-------+
-- | id   | revenue | month |
-- +------+---------+-------+
-- | 1    | 8000    | Jan   |
-- | 2    | 9000    | Jan   |
-- | 3    | 10000   | Feb   |
-- | 1    | 7000    | Feb   |
-- | 1    | 6000    | Mar   |
-- +------+---------+-------+
-- Output: 
-- +------+-------------+-------------+-------------+-----+-------------+
-- | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
-- +------+-------------+-------------+-------------+-----+-------------+
-- | 1    | 8000        | 7000        | 6000        | ... | null        |
-- | 2    | 9000        | null        | null        | ... | null        |
-- | 3    | null        | 10000       | null        | ... | null        |
-- +------+-------------+-------------+-------------+-----+-------------+
select id,
	max(case when month = 'Jan' then revenue end) as Jan_Revenue,
	max(case when month = 'Feb' then revenue end) as Feb_Revenue,
	max(case when month = 'Mar' then revenue end) as Mar_Revenue,
	max(case when month = 'Apr' then revenue end) as Apr_Revenue,
	max(case when month = 'May' then revenue end) as May_Revenue,
	max(case when month = 'Jun' then revenue end) as Jun_Revenue,
	max(case when month = 'Jul' then revenue end) as Jul_Revenue,
	max(case when month = 'Aug' then revenue end) as Aug_Revenue,
	max(case when month = 'Sep' then revenue end) as Sep_Revenue,
	max(case when month = 'Oct' then revenue end) as Oct_Revenue,
	max(case when month = 'Nov' then revenue end) as Nov_Revenue,
	max(case when month = 'Dec' then revenue end) as Dec_Revenue
from Department
group by id
order by id