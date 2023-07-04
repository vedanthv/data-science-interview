### Simple SQL Query Based Questions

1. SQL Query to Find Second Highest Salary Of Employee

```sql
SELECT MAX(Salary) 
FROM Employee 
WHERE Salary NOT IN (select MAX(Salary) from Employee ); 
```

2. SQL Query to Find Max Salary From Each Department

```sql
select dept_id,max(salary)
from employee
group by dept_id  
```

3. Write SQL Query to output the max salary along with the department

```sql
SELECT DeptName, MAX(Salary) 
FROM Employee e RIGHT JOIN Department d 
ON e.DeptId = d.DeptID 
GROUP BY DeptName;
```
In this query, we have used RIGHT OUTER JOIN because we need the name of the department from the Department table which is on the right side of the JOIN clause, even if there is no reference of dept_id on the Employee table. 

4. How to print the current date?

```sql
SELECT GetDate(); 
```

5. Write SQL query to check if the date is in the correct format?

```sql
SELECT  ISDATE('1/08/13') AS "MM/DD/YY"; 
```

6. Write an SQL Query to print the name of the distinct employee whose DOB is between 01/01/1960 to 31/12/1975.

```sql
SELECT DISTINCT emp_name
FROM employees
WHERE DOB BETWEEN "01-06-1970" AND "31-12-2000"
```

7. Write an SQL Query to find the number of employees according to gender whose DOB is between 01/01/1960 to 31/12/1975.

```sql
SELECT COUNT(*), sex FROM Employees WHERE DOB BETWEEN '01/02/1971' AND '31/12/1975' GROUP BY sex;
```

8. find all Employee records containing the word "Joe", regardless of whether it was stored as JOE, Joe, or joe.

```sql
SELECT * from Employees  WHERE  UPPER(EmpName) like '%JOE%';
```

9. Write an SQL Query to find the year from date.

```sql
SELECT YEAR(GETDATE()) as "Year";
```

10. Query to find duplicate entries and delete them

```sql
DELETE FROM produce WHERE
(SELECT name,category,
FROM product
GROUP BY name, category
HAVING COUNT(id) >1);
```

11. There is a table which contains two columns Student and Marks, you need to find all the students, whose marks are greater than average marks i.e. list of above-average students.

```sql
SELECT student, marks 
FROM table 
WHERE marks > (SELECT AVG(marks) from table)
```

12. How do you find all employees who are also managers?

```sql
SELECT e.name, m.name 
FROM Employee e, Employee m 
WHERE e.mgr_id = m.emp_id;
```

