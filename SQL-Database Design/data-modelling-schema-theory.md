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


