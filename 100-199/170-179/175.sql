--  Table: Person                 Table: Address
--  +-------------+---------+     +-------------+---------+
--  | Column Name | Type    |     | Column Name | Type    |
--  +-------------+---------+     +-------------+---------+
--  | PersonId    | int     |     | AddressId   | int     |
--  | FirstName   | varchar |     | PersonId    | int     |
--  | LastName    | varchar |     | City        | varchar |
--  +-------------+---------+     | State       | varchar |
--                                +-------------+---------+
--
--  Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If
--  the address of a PersonId is not present in the Address table, report null instead. Return the result table in
--  any order.
--
--  The query result format is in the following example.
--
--  Example 1:
--  Input:
--  Person table:                          Address table:
--  +----------+----------+-----------+    +-----------+----------+---------------+------------+
--  | PersonId | LastName | FirstName |    | AddressId | PersonId | City          | State      |
--  +----------+----------+-----------+    +-----------+----------+---------------+------------+
--  | 1        | Wang     | Allen     |    | 1         | 2        | New York City | New York   |
--  | 2        | Alice    | Bob       |    | 2         | 3        | Leetcode      | California |
--  +----------+----------+-----------+    +-----------+----------+---------------+------------+
--  Output:
--  +-----------+----------+---------------+----------+
--  | FirstName | LastName | City          | State    |
--  +-----------+----------+---------------+----------+
--  | Allen     | Wang     | Null          | Null     |
--  | Bob       | Alice    | New York City | New York |
--  +-----------+----------+---------------+----------+
--  Explanation:
--  There is no address in the address table for the PersonId = 1 so we return null in their city and state.
--  AddressId = 1 contains information about the address of PersonId = 2.


select p.FirstName, p.LastName, a.City, a.State
from Person p
left join Address a on a.personId = p.personId
