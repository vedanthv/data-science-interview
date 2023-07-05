## Easy SQL Theory Concepts

1. Which TCP/IP port does SQL Server run on? How can it be changed?

SQL Server runs on port 1433. It can be changed from the Network Utility TCP/IP properties.

2. What is the difference between primary key and unique key?

Both primary key and unique key enforces uniqueness of the column on which they are defined. But by default primary key creates a clustered index on the column, where are unique creates a nonclustered index by default. Another major difference is that, primary key doesn't allow NULLs, but unique key allows one NULL only.

3. What is the difference between truncate and delete?

Delete command removes the rows from a table based on the condition that we provide with a WHERE clause. Truncate will actually remove all the rows from a table and there will be no data in the table after we run the truncate command.

- Truncate is a DDL Command whereas delete is a DML command
- TRUNCATE is faster and uses fewer system and transaction log resources than DELETE.
- DELETE removes rows one at a time and records an entry in the transaction log for each deleted row.
- DELETE and TRUNCATE both can be rolled back when surrounded by TRANSACTION if the current session is not closed.

4. What is the difference between a HAVING CLAUSE and a WHERE CLAUSE?

They specify a search condition for a group or an aggregate. But the difference is that HAVING can be used only with the SELECT statement. HAVING is typically used in a GROUP BY clause. When GROUP BY is not used, HAVING behaves like a WHERE clause. Having Clause is basically used only with the GROUP BY function in a query whereas WHERE Clause is applied to each row before they are part of the GROUP BY function in a query.

5. Can subquery have order by clause? 

No it cannot have order by clause in it but can be nested

6. What is log shipping?

Log shipping is the process of automating the backup of database and transaction log files on a production SQL server, and then restoring them onto a standby server.

7. What is the difference between stuff and replace function?

STUFF function is used to overwrite existing characters. Using this syntax, STUFF (string_expression, start, length, replacement_characters), string_expression is the string that will have characters substituted, start is the starting position, length is the number of characters in the string that are substituted, and replacement_characters are the new characters interjected into the string. 

REPLACE function to replace existing characters of all occurrences.

8. What is FOREIGN KEY?

A FOREIGN KEY constraint prevents any actions that would destroy links between tables with the corresponding data values. A foreign key in one table points to a primary key in another table.

Foreign keys prevent actions that would leave rows with foreign key values when there are no primary keys with that value. The foreign key constraints are used to enforce referential integrity.

9. What is the NOT NULL Constraint?

A NOT NULL constraint enforces that the column will not accept null values. The not null constraints are used to enforce domain integrity, as the check constraints.

10. What are the advantages of stored procedures?

Stored procedure can reduced network traffic and latency, boosting application performance. Stored procedure execution plans can be reused, staying cached in SQL Server's memory, reducing server overhead.

11. What is bulk copy command?

BulkCopy is a tool used to copy huge amount of data from tables and views. BCP does not copy the structures same as source to destination. BULK INSERT command helps to import a data file into a database table or view in a user-specified format.

12. How to implement the different kinds of relationships?

One-to-One relationship can be implemented as a single table and rarely as two tables with primary and foreign key relationships. 

One-to-Many relationships are implemented by splitting the data into two tables with primary key and foreign key relationships. 

Many-to-Many relationships are implemented using a junction table with the keys from both the tables forming the composite primary key of the junction table.

13. What is Execution Plan?

An execution plan is basically a road map that graphically or textually shows the data retrieval methods chosen by the SQL Server query optimizer for a stored procedure or ad- hoc query and is a very useful tool for a developer to understand the performance characteristics of a query or stored procedure.

14. What are the various DDL Commands?

Create, Alter and Drop are the various DDL Commands.

15. What are the various DML Commands in SQL?

Select, Insert, Update and Delete

16. What is the difference between cross and natural joins?

Cross Join produces the cross product between two tables and the natural join joins the columns with the same name.

17. What's wrong in the following statement?

```sql
SELECT subject_code,AVG(marks)
FROM students
WHERE AVG(marks) > 75
GROUP BY subject_code
```

We cannot use where clause to restrict groups. Having must be used.

```sql
SELECT subject_code, AVG (marks)
   FROM students
   HAVING AVG(marks) > 75
   GROUP BY subject_code;
```

18. Can group functions be nested?

Yes they can be nested in a depth of 2.

19. What is wrong in the following code?

```sql
SELECT student_code, name
   FROM students
   WHERE marks = 
               (SELECT MAX(marks)
                  FROM students
                  GROUP BY subject_code);
```

Single = is used here for multiple results in the inner sub query. We have to use IN operator.

20. Can you modify the rows in a table based on values from another table? Explain.

Yes. Use of subqueries in UPDATE statements allow you to update rows in a table based on values from another table.

21. You can use subquey inside insert function?

Yes we can. Example is : 

```sql
INSERT INTO agent1
SELECT * FROM  agents
WHERE agent_code=ANY(
SELECT agent_code FROM customer
WHERE cust_country="UK");
```

22. **What is the use of merge statement?**

The MERGE statement allows conditional update or insertion of data into a database table. It performs an UPDATE if the rows exists, or an INSERT if the row does not exist.

Read [this](https://www.scaler.com/topics/merge-in-sql/)

```sql
MERGE target_table USING source_table
ON merge_condition
WHEN MATCHED
    THEN update_statement
WHEN NOT MATCHED
    THEN insert_statement
WHEN NOT MATCHED BY SOURCE
    THEN DELETE;
```

23. What is a view? Why should we use a view?

A view is a logical snapshot based on a table or another view. It is used for −

- Restricting access to data;
- Making complex queries simple;
- Ensuring data independency;
- Providing different views of same data.

A view doesnt have data of its own