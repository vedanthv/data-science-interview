## Data Science Interview Prep

### DBMS Questions
1. **What is SQL?**
   
It stands for Structured Query Language. A programming language used for interaction with relational database management systems (RDBMS). This includes fetching, updating, inserting, and removing data from tables.

2. **What are some SQL Dialects?**

The various versions of SQL, both free and paid, are also called SQL dialects. All the flavors of SQL have a very similar syntax and vary insignificantly only in additional functionality. Some examples are Microsoft SQL Server, PostgreSQL, MySQL, SQLite, T-SQL, Oracle, and MongoDB.

3. **What are the types of SQL Statements?**

- Data Definition Language (DDL) – to define and modify the structure of a database.
- Data Manipulation Language (DML) – to access, manipulate, and modify data in a database.
- Data Control Language (DCL) – to control user access to the data in the database and give or revoke privileges to a specific user or a group of users.
- Transaction Control Language (TCL) – to control transactions in a database.
- Data Query Language (DQL) – to perform queries on the data in a database to retrieve the necessary information from it.

4. **Examples of Common SQL Commands?**

- DDL: CREATE, ALTER TABLE, DROP, TRUNCATE, and ADD COLUMN
- DML: UPDATE, DELETE, and INSERT
- DCL: GRANT and REVOKE
- TCL: COMMIT, SET TRANSACTION, ROLLBACK, and SAVEPOINT
- DQL: – SELECT

5. **What is a Database?**

A structured storage space where the data is kept in many tables and organized so that the necessary information can be easily fetched, manipulated, and summarized.

6. **What is a DBMS?**

It stands for Database Management System, a software package used to perform various operations on the data stored in a database, such as accessing, updating, wrangling, inserting, and removing data. There are various types of DBMS, such as relational, hierarchical, network, graph, or object-oriented. These types are based on the way the data is organized, structured, and stored in the system.

7. **What is RDBMS?**

It stands for Relational Database Management System. It's the most common type of DBMS used for working with data stored in multiple tables related to each other by means of shared keys. The SQL programming language is particularly designed to interact with RDBMS. Some examples of RDBMS are MySQL, PostgreSQL, Oracle, MariaDB, etc.

8. **What is a sub query?**

Also called an inner query; a query placed inside another query, or an outer query. A subquery may occur in the clauses such as SELECT, FROM, WHERE, UPDATE, etc. It's also possible to have a subquery inside another subquery. The innermost subquery is run first, and its result is passed to the containing query (or subquery).

9. **What are the types of Sub Queries?**

- Single-row – returns at most one row.
- Multi-row – returns at least two rows.
- Multi-column – returns at least two columns.
- Correlated – a subquery related to the information from the outer query.
- Nested – a subquery inside another subquery.

10. **What are constraints in SQL?**

A set of conditions defining the type of data that can be input into each column of a table. Constraints ensure data integrity in a table and block undesired actions.

11. **What SQL constraints do you know?**

- DEFAULT – provides a default value for a column.
- UNIQUE – allows only unique values.
- NOT NULL – allows only non-null values.
- PRIMARY KEY – allows only unique and strictly non-null values (NOT NULL and UNIQUE).
- FOREIGN KEY – provides shared keys between two and more tables.

12. **What are joins in SQL?**

A clause used to combine and retrieve records from two or multiple tables. SQL tables can be joined based on the relationship between the columns of those tables. Check out our SQL joins tutorial for more context. 

13. **What are the types of Joins in SQL?**

- (INNER) JOIN – returns only those records that satisfy a defined join condition in both (or all) tables. It's a default SQL join.
- LEFT (OUTER) JOIN – returns all records from the left table and those records from the right table that satisfy a defined join condition.
- RIGHT (OUTER) JOIN – returns all records from the right table and those records from the left table that satisfy a defined join condition.
- FULL (OUTER) JOIN – returns all records from both (or all) tables. It can be considered as a combination of left and right joins.

14. **What is Primary Key in SQL?**

A column (or multiple columns) of a table to which the PRIMARY KEY constraint was imposed to ensure unique and non-null values in that column. In other words, a primary key is a combination of the NOT NULL and UNIQUE constraints. 

The primary key uniquely identifies each record of the table. Each table should contain a primary key and can't contain more than one primary key.

15. **What is a Unique Key in SQL?**

A column (or multiple columns) of a table to which the UNIQUE constraint was imposed to ensure unique values in that column, including a possible NULL value (the only one).

16. **What is a foreign key in SQL?**

A column (or multiple columns) of a table to which the FOREIGN KEY constraint was imposed to link this column to the primary key in another table (or several tables). The purpose of foreign keys is to keep connected various tables of a database.

17. **What is a CTE?**

A CTE is a data set that is created temporarily and can be used within a query. It is available for use during the entire session of the query execution. On the other hand, a subquery is a query nested within another query and can only be used within that query. A subquery typically acts as a column with a single value in the FROM or WHERE clause.

The benefits of using a CTE are that it is more readable and can be reused throughout the query session, whereas a subquery can only be used within the query in which it is defined.

