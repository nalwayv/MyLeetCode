-- 181. Employees Earning More Than Their Managers
-- Employee table:
-- +----+-------+--------+-----------+
-- | id | name  | salary | managerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+

SELECT personA.name AS 'Employee'
FROM Employee AS personA
JOIN Employee personB ON personA.managerid = personB.id
WHERE personA.salary > personB.salary