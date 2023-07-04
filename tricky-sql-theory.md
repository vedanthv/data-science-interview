### Some tricky SQL Theory Questions

1. What is the difference between union and union all?

UNION merges the contents of two structurally-compatible tables into a single combined table. The difference between UNION and UNION ALL is that UNION will omit duplicate records whereas UNION ALL will include duplicate records.

It is important to note that the performance of UNION ALL will typically be better than UNION, since UNION requires the server to do the additional work of removing any duplicates. So, in cases where is is certain that there will not be any duplicates, or where having duplicates is not a problem, use of UNION ALL would be recommended for performance reasons.

2. What is the result of the query?

sql> SELECT * FROM runners;
+----+--------------+
| id | name         |
+----+--------------+
|  1 | John Doe     |
|  2 | Jane Doe     |
|  3 | Alice Jones  |
|  4 | Bobby Louis  |
|  5 | Lisa Romero  |
+----+--------------+

sql> SELECT * FROM races;
+----+----------------+-----------+
| id | event          | winner_id |
+----+----------------+-----------+
|  1 | 100 meter dash |  2        |
|  2 | 500 meter dash |  3        |
|  3 | cross-country  |  2        |
|  4 | triathalon     |  NULL     |
+----+----------------+-----------+

```sql
SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races)
```

Surprisingly, given the sample data provided, the result of this query will be an empty set. The reason for this is as follows: 

If the set being evaluated by the SQL NOT IN condition contains any values that are null, then the outer query here will return an empty set, even if there are many runner ids that match winner_ids in the races table.

This query will return only the queries where the winner id is null

```sql
SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races WHERE winner_id IS NOT null)
```

3. Assume a schema of Emp ( Id, Name, DeptId ) , Dept ( Id, Name).

If there are 10 records in the Emp table and 5 records in the Dept table, how many rows will be displayed in the result of the following SQL query:

```sql
Select * From Emp, Dept
```
The query will result in 50 rows as a “cartesian product” or “cross join”, which is the default whenever the ‘where’ clause is omitted.

4. Write a query to fetch values in table test_a that are and not in test_b without using the NOT keyword.

```sql
insert into test_a(id) values (10);
insert into test_a(id) values (20);
insert into test_a(id) values (30);
insert into test_a(id) values (40);
insert into test_a(id) values (50);
insert into test_b(id) values (10);
insert into test_b(id) values (30);
insert into test_b(id) values (50);
```

**Answer**

```sql
select a.id
from test_a a
left join test_b b on a.id = b.id
where b.id is null;
```

5. Write a SQL query to find the 10th highest employee salary from an Employee table. Explain your answer.

```sql
SELECT Salary FROM
(
    SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 10
) AS Emp ORDER BY Salary LIMIT 1;
```

6. How to remove duplicates with UNION ALL?

```sql
select * from (
select * from table1
union all 
select * from table2
) a group by 
columns
having count(*) >= 1
```

7. Given the below tables write a query to to get the list of users who took the a training lesson more than once in the same day, grouped by user and training lesson, each ordered from the most recent lesson date to oldest date.

SELECT * FROM users;

user_id  username
1        John Doe                                                                                            
2        Jane Don                                                                                            
3        Alice Jones                                                                                         
4        Lisa Romero

SELECT * FROM training_details;

user_training_id  user_id  training_id  training_date
1                 1        1            "2015-08-02"
2                 2        1            "2015-08-03"
3                 3        2            "2015-08-02"
4                 4        2            "2015-08-04"
5                 2        2            "2015-08-03"
6                 1        1            "2015-08-02"
7                 3        2            "2015-08-04"
8                 4        3            "2015-08-03"
9                 1        4            "2015-08-03"
10                3        1            "2015-08-02"
11                4        2            "2015-08-04"
12                3        2            "2015-08-02"
13                1        1            "2015-08-02"
14                4        3            "2015-08-03"

```sql
SELECT
      u.user_id,
      username,
      training_id,
      training_date,
      count( user_training_id ) AS count
  FROM users u JOIN training_details t ON t.user_id = u.user_id
  GROUP BY u.user_id,
           username,
           training_id,
           training_date
  HAVING count( user_training_id ) > 1
  ORDER BY training_date DESC;
```

8. What is an execution plan in SQL?

An execution plan is basically a road map that graphically or textually shows the data retrieval methods chosen by the SQL server’s query optimizer for a stored procedure or ad hoc query. Execution plans are very useful for helping a developer understand and analyze the performance characteristics of a query or stored procedure, since the plan is used to execute the query or stored procedure.

9. What are ACID Properties in RDBMS?

Atomicity. Atomicity requires that each transaction be “all or nothing”: if one part of the transaction fails, the entire transaction fails, and the database state is left unchanged. An atomic system must guarantee atomicity in each and every situation, including power failures, errors, and crashes.

Consistency. The consistency property ensures that any transaction will bring the database from one valid state to another. Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof.

Isolation. The isolation property ensures that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other. Providing isolation is the main goal of concurrency control. Depending on concurrency control method (i.e. if it uses strict - as opposed to relaxed - serializability), the effects of an incomplete transaction might not even be visible to another transaction.

Durability. Durability means that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors. In a relational database, for instance, once a group of SQL statements execute, the results need to be stored permanently (even if the database crashes immediately thereafter). To defend against power loss, transactions (or their effects) must be recorded in a non-volatile memory.

10. Given a table dbo.users where the column user_id is a unique numeric identifier, how can you efficiently select the first 100 odd user_id values from the table?

(Assume the table contains well over 100 records with odd user_id values.)

```sql
SELECT TOP 100 user_id FROM dbo.users WHERE user_id % 2 = 1 ORDER BY user_id
```

11. What are the NVL and the NVL2 functions in SQL? How do they differ?

Both the NVL(exp1, exp2) and NVL2(exp1, exp2, exp3) functions check the value exp1 to see if it is null.

With the NVL(exp1, exp2) function, if exp1 is not null, then the value of exp1 is returned; otherwise, the value of exp2 is returned, but case to the same data type as that of exp1.

With the NVL2(exp1, exp2, exp3) function, if exp1 is not null, then exp2 is returned; otherwise, the value of exp3 is returned.

12. What is the difference between rank and dense rank?

The only difference between the RANK() and DENSE_RANK() functions is in cases where there is a “tie”; i.e., in cases where multiple values in a set have the same ranking. 

In such cases, RANK() will assign non-consecutive “ranks” to the values in the set (resulting in gaps between the integer ranking values when there is a tie), whereas DENSE_RANK() will assign consecutive ranks to the values in the set (so there will be no gaps between the integer ranking values in the case of a tie).

13. What is the difference between WHERE and HAVING clause?

When GROUP BY is not used, the WHERE and HAVING clauses are essentially equivalent.

However, when GROUP BY is used:

The WHERE clause is used to filter records from a result. The filtering occurs before any groupings are made.
The HAVING clause is used to filter values from a group (i.e., to check conditions after aggregation into groups has been performed).

14. Given a table Employee having columns empName and empId, what will be the result of the SQL query below?

```sql
select empName from Employee order by 2 desc;
```

The query wont execute as the column numbering starts from 0 and there are only two columns in the table


15. What will be the output of the below query, given an Employee table having 10 records?

```sql
BEGIN TRAN
TRUNCATE TABLE Employees
ROLLBACK
SELECT * FROM Employees
```

The 10 records will be the output as transactions keep a log of the commands executed.

16. Imagine a single column in a table that is populated with either a single digit (0-9) or a single character (a-z, A-Z). Write a SQL query to print ‘Fizz’ for a numeric value or ‘Buzz’ for alphabetical value for all values in that column.

```sql
SELECT col, CASE WHEN upper(col) = lower(col) THEN "Fizz" ELSE "Buzz" END AS FizzBuzz FROM table;
```

17. What is the difference between char and varachar2?

When stored in a database, varchar2 uses only the allocated space. E.g. if you have a varchar2(1999) and put 50 bytes in the table, it will use 52 bytes.

But when stored in a database, char always uses the maximum length and is blank-padded. E.g. if you have char(1999) and put 50 bytes in the table, it will consume 2000 bytes.

18. Given this table

Testdb=# Select * FROM "Test"."EMP";

 ID
----
  1
  2
  3
  4
  5
(5 rows)

19. What will be the output of the below snippet?

```sql
Select SUM(1) FROM "Test"."EMP";
Select SUM(2) FROM "Test"."EMP";
Select SUM(3) FROM "Test"."EMP";
```
**Ans: 5 10 15**

20. Table is as follows:

ID	C1	C2	C3
1	Red	Yellow	Blue
2	NULL	Red	Green
3	Yellow	NULL	Violet
Print the rows which have ‘Yellow’ in one of the columns C1, C2, or C3, but without using OR.

```sql
SELECT * FROM table
WHERE 'Yellow' IN (C1, C2, C3)
```

21. Write a query to insert/update Col2’s values to look exactly opposite to Col1’s values.

Col1	Col2
1	0
0	1
0	1
0	1
1	0
0	1
1	0
1	0

```sql
update table set col2 = case when col1 = 1 then 0 else 1 end
```

