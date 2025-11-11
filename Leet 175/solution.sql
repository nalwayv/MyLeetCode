-- 175. Combine Two Tables

-- PERSON
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+

-- ADDRESS
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+

SELECT 
    Person.firstName,
    Person.lastName,
    Address.City,
    Address.State
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId