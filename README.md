## Data Science Interview Prep

### Basic SQL Questions

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

18. **What is an index?**

A special data structure related to a database table and used for storing its important parts and enabling faster data search and retrieval. Indexes are especially efficient for large databases, where they significantly enhance query performance.

19. **What are the types of indices?**

- Unique index – doesn't allow duplicates in a table column and hence helps maintain data integrity.

- Clustered index – defines the physical order of records of a database table and performs data searching based on the key values. A table can have only one clustered index.

- Non-clustered index – keeps the order of the table records that doesn't match the physical order of the actual data on the disk. It means that the data is stored in one place and a non-clustered index – in another one. A table can have multiple non-clustered indexes.

20. **What is an SQL Schema?**

A collection of database structural elements such as tables, stored procedures, indexes, functions, and triggers. It shows the overall database architecture, specifies the relationships between various objects of a database, and defines different access permissions for them.

21. **What is a schema?**

A collection of database structural elements such as tables, stored procedures, indexes, functions, and triggers. It shows the overall database architecture, specifies the relationships between various objects of a database, and defines different access permissions for them.

22. **What is SQL Operator?**

A reserved character, a combination of characters, or a keyword used in SQL queries to perform a specific operation. SQL operators are commonly used with the WHERE clause to set a condition (or conditions) for filtering the data.

23. **What is SQL Clause?**

A condition imposed on a SQL query to filter the data to obtain the desired result. Some examples are WHERE, LIMIT, HAVING, LIKE, AND, OR, ORDER BY, etc.

24. **How to Select Common Records from two tables?**

```sql
SELECT * FROM table_1
INTERSECT
SELECT * FROM table_1;
```

25. What are entities?

An entity is a real-world object, creature, place, or phenomenon for which the data can be gathered and stored in a database table. Each entity corresponds to a row in a table, while the table's columns describe its properties. Some examples of entities are bank transactions, students in a school, cars sold, etc.

26. What are relationships? Give some examples?

Relationships are the connections and correlations between entities, basically meaning how two or more tables of a database are related to one another. For example, we can find an ID of the same client in a table on sales data and in a customer table.

27. What is NULL Value?

A NULL value indicates the absence of data for a certain cell of a table. Instead, zero is a valid numeric value, and an empty string is a legal string of zero length.

28. What is a function in SQL?

A database object representing a set of SQL statements frequently used for a certain task. A function takes in some input parameters, performs calculations or other manipulations on them, and returns the result. Functions help improve code readability and avoid repetition of the same code snippets.

29. What are the types of functions in SQL?

- Aggregate functions – work on multiple, usually grouped records for the provided columns of a table, and return a single value (usually by group).
- Scalar functions – work on each individual value and return a single value.

30. Give examples of aggregate and scalar functions?

- aggregate : sum,avg,min,max
- scalar : len,ucase,lcase,initcap,mid/substr,round,now

31. Give examples of character manipulation functions?

- concat, substr,len,replace,lpad,rpad,trim

32. What are some set operations in SQL?

- UNION, UNION ALL, INTERSECT, EXCEPT

33. How to Pattern Match in SQL?

The LIKE operator in combination with the % and _ wildcards. The % wildcard represents any number of characters including zero, while _ – strictly one character.

34. What is the difference between a primary key and a unique key?

While both types of keys ensure unique values in a column of a table, the first one identifies uniquely each record of the table, and the second one prevents duplicates in that column.

35. Can primary keys be based on multiple columns?

Yes its called composite primary key.

36. What is the order of appearance of the common statements in the SELECT query?

```
SELECT-FROM-JOIN-ON-WHERE-GROUP BY-HAVING-ORDER BY-LIMIT
```

37. In which order the interpreter executes the common statements in the SELECT query?

```
FROM-JOIN-ON-WHERE-GROUP BY-HAVING-SELECT-ORDER BY-LIMIT
```

38. What is a view and why we should use it?


A virtual table containing a subset of data retrieved from one or more database tables (or other views). Views take very little space, simplify complex queries, limit access to the data for security reasons, enable data independence, and summarize data from multiple tables.


39. Can we create a view after the table is deleted?


No. Any views based on that table will become invalid after deleting the base table. If we try to use such a view anyway, we'll receive an error message.


40. What are the different types of SQL Relationships?

- One-to-one – each record in one table corresponds to only one record in another table
- One-to-many – each record in one table corresponds to several records in another table
- Many-to-many – each record in both tables corresponds to several records in another table

41. What are the possible values of the boolean data field?

In some SQL flavors, such as PostgreSQL, the BOOLEAN data type exists explicitly and takes values TRUE, FALSE, or NULL. In other flavors, such as Microsoft SQL Server, the BIT datatype is used to store Boolean values as integers 1 (true) or 0 (false).

41. What is normalization in SQL, and why use it?

Normalization is a process of database design that includes organizing and restructuring data in a way to reduce data redundancy, dependency, duplication, and inconsistency. This leads to enhanced data integrity, more tables within the database, more efficient data access and security control, and greater query flexibility.

42. What is denormalization in SQL?

Denormalization is the process opposite of normalization: it introduces data redundancy and combines data from multiple tables. Denormalization optimizes the performance of the database infrastructure in situations when read operations are more important than write operations since it helps avoid complex joins and reduces the time of query running.

43. What is the difference between nested and correlated subqueries?

A correlated subquery is an inner query nested in a bigger (outer) query that refers to the values from the outer query for its execution, meaning that a correlated subquery depends on its outer query. Instead, a non-correlated subquery doesn't rely on the data from the outer query and can be run independently of it.

44. What is the difference between delete and truncate statements?

DELETE is a reversible DML (Data Manipulation Language) command used to delete one or more rows from a table based on the conditions specified in the WHERE clause. 

Instead, TRUNCATE is an irreversible DDL (Data Definition Language) command used to delete all rows from a table. DELETE works slower than TRUNCATE. 

Also, we can't use the TRUNCATE statement for a table containing a foreign key.

45. What is the difference between the DROP and TRUNCATE statements?

DROP deletes a table from the database completely, including the table structure and all the associated constraints, relationships with other tables, and access privileges. 

TRUNCATE deletes all rows from a table without affecting the table structure and constraints. 

DROP works slower than TRUNCATE. Both are irreversible DDL (Data Definition Language) commands.

46. What is the difference between the HAVING and WHERE statements?

The first one works on aggregated data after they are grouped, while the second one checks each row individually. 

If both statements are present in a query, they appear in the following order: WHERE – GROUP BY – HAVING. The SQL engine interprets them also in the same order.

47. How to Rename a Column in SQL?

```sql
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```

48. How to Delete a column from table?

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

49. How to select all even records from the table?

```sql
SELECT * FROM table_name 
WHERE ID_column % 2 = 0;
```

50. How to find nth highest value in the table?

```sql
SELECT * FROM table_name
ORDER BY column_name DESC
LIMIT 1
OFFSET 5;
```

51. How to find a value in text column that starts with a letter?

```sql
SELECT * FROM table_name
WHERE surname LIKE 'A%';
```

52. How to find the last id in a table?

```sql
SELECT id
FROM table_name
ORDER BY id DESC
LIMIT 1;
```

53. How to select random rows from a table?

```sql
SELECT * FROM table_name
ORDER BY RAND()
LIMIT 5;
```

### Data Modelling Questions

1. What do you understand by data modelling?

Data Modelling is the diagrammatic representation showing how the entities are related to each other. It is the initial step towards database design. We first create the conceptual model, then the logical model and finally move to the physical model.

Generally, the data models are created in data analysis & design phase of software development life cycle.

2. What are the types of Data Models?

There are three types of data models – conceptual, logical and physical. The level of complexity and detail increases from conceptual to logical to a physical data model.

The conceptual model shows a very basic high level of design while the physical data model shows a very detailed view of design.

Conceptual Model will be just portraying entity names and entity relationships. Figure 1 shown in the later part of this article depicts a conceptual model.
Logical Model will be showing up entity names, entity relationships, attributes, primary keys and foreign keys in each entity. Figure 2 shown inside question#4 in this article depicts a logical model.
Physical Data Model will be showing primary keys, foreign keys, table names, column names and column data types. This view actually elaborates how the model will be actually implemented in the database.

3. What are the types of Database Design Schemas in Data Modelling?

There are two different kinds of schemas in data modeling

- Star Schema
- Snowflake Schema

The simplest of the schemas is star schema where we have a fact table in the center that references multiple dimension tables around it. All the dimension tables are connected to the fact table. The primary key in all dimension tables acts as a foreign key in the fact table.

4. What are the components of Star Schema?

Fact table: It contains the quantitative and numeric data that represents the business events or measurements. The fact table typically consists of foreign keys that reference the primary keys of the dimension tables, as well as the measures or metrics associated with the business process being analyzed.

Dimension tables: These tables provide descriptive attributes or context for the data stored in the fact table. Dimension tables contain the textual or categorical data that help in analyzing and filtering the facts. 

Each dimension table represents a specific aspect or viewpoint of the business, such as time, geography, product, customer, or any other relevant entity. Dimension tables are connected to the fact table through foreign key relationships.

Foreign keys: They are the primary keys from dimension tables that are used in the fact table to establish relationships between the fact and dimension data. The foreign keys in the fact table help in joining the data from multiple dimension tables to perform complex queries and analysis.

5. What is Snowflake Schema?

In a snowflake schema, the level of normalization increases. The fact table here remains the same as in the star schema. However, the dimension tables are normalized. 

Due to several layers of dimension tables, it looks like a snowflake, and thus it is named as snowflake schema.

6. What is the difference between star and snowflake schema?

Since star schema is in de-normalized form, you require fewer joins for a query. The query is simple and runs faster in a star schema. 

Coming to the snowflake schema, since it is in normalized form, it will require a number of joins as compared to a star schema, the query will be complex and execution will be slower than star schema.

Another significant difference between these two schemas is that snowflake schema does not contain redundant data and thus it is easy to maintain. 

On the contrary, star schema has a high level of redundancy and thus it is difficult to maintain.

7. When to use which schema?

Now, which one to choose for your project? If the purpose of your project is to do more of dimension analysis, you should go for snowflake schema. For Example, if you need to find out that “how many subscribers are tied to a particular plan which is currently active?” – go with the snowflake model.

If the purpose of your project is to do more of a metrics analysis, you should go with a star schema. For Example, if you need to find out that “what is the claim amount paid to a particular subscriber?” – go with a star schema.

8. What is a dimension and attribute?

Dimensions represent qualitative data. For Example, plan, product, class are all dimensions.

A dimension table contains descriptive or textual attributes. For Example, the product category & product name are the attributes of the product dimension.

9. What is a fact and fact table?

Facts represent quantitative data.

For Example, the net amount due is a fact. A fact table contains numerical data and foreign keys from related dimensional tables.

10. What is a factless fact table?

Factless fact table is a fact table that contains no fact measure in it. It has only the dimension keys in it.

At times, certain situations may arise in the business where you need to have a factless fact table.

11. What is the diffrence between OLTP and OLAP?

OLTP stands for the Online Transaction Processing System & OLAP stands for the Online Analytical Processing System. OLTP maintains the transactional data of the business & is highly normalized generally. On the contrary, OLAP is for analysis and reporting purposes & it is in de-normalized form.

This difference between OLAP and OLTP also gives you the way to choosing the design of schema. If your system is OLTP, you should go with star schema design and if your system is OLAP, you should go with snowflake schema.

12. What is a data mart?

Data marts are for the most part intended for a solitary branch of business. They are designed for the individual departments.

For Example, I used to work for a health insurance provider company that had different departments in it like Finance, Reporting, Sales and so forth.

We had a data warehouse that was holding the information pertaining to all these departments and then we have few data marts built on top of this data warehouse. These DataMart were specific to each department. In simple words, you can say that a DataMart is a subset of a data warehouse.

13. What are the types of measures?

- Non-additive measures are the ones on top of which no aggregation function can be applied. For Example, a ratio or a percentage column; a flag or an indicator column present in fact table holding values like Y/N, etc. is a non-additive measure.

- Semi- additive measures are the ones on top of which some (but not all) aggregation functions can be applied. For Example, fee rate or account balance.

- Additive measures are the ones on top of which all aggregation functions can be applied. For Example, units purchased.

14. Have you ever came across the scenario of recursive relationships? If yes, how did you handle it?

A recursive relationship occurs in the case where an entity is related to itself. Yes, I have come across such a scenario.

Talking about the health care domain, it is a possibility that a health care provider (say, a doctor) is a patient to any other health care provider. Because, if the doctor himself falls ill and needs surgery, he will have to visit some other doctor for getting the surgical treatment.

So, in this case, the entity – health care provider is related to itself. A foreign key to the health insurance provider’s number will have to present in each member’s (patient) record.

15. What are few common mistakes in data modelling?

- Building Massive Models
- Lack of Purpose
- Unnecessary De Normalization

16. Employee health details are hidden from his employer by the health care provider. Which level of data hiding is this? Conceptual, physical or external?

This is the scenario of an external level of data hiding.

17. What is the form of fact table & dimension table?

Generally fact table is denormalized and dimension table is normalized.

18. Tricky one:  If a unique constraint is applied to a column then will it throw an error if you try to insert two nulls into it?

Yes we can have two nulls because all null values are distinct.

19. What is the significance of metadata?

Metadata is data about data. It tells you what kind of data is actually stored in the system, what is its purpose and for whom it is intended.


