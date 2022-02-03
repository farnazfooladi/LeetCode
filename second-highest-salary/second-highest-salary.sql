# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT Salary 
                FROM Employee
                ORDER BY Salary DESC
                LIMIT 1)