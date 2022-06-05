/* Write your T-SQL query statement below */
select max(salary) as 'SecondHighestSalary' from Employee
where Salary < (select max(Salary) from Employee)