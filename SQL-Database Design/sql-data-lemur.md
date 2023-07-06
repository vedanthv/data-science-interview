### Data Lemur SQL Questions

#### 1. Pages with No Likes

Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").

Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs.

```sql
SELECT pages.page_id
FROM pages
LEFT OUTER JOIN page_likes AS likes
  ON pages.page_id = likes.page_id
WHERE likes.page_id IS NULL;
```

```sql
SELECT page_id
FROM pages
WHERE page_id NOT IN (
  SELECT page_id
  FROM page_likes
  WHERE page_id IS NOT NULL
);
```

#### 2. Unfinished Parts

Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query that determines which parts with the assembly steps have initiated the assembly process but remain unfinished.

```sql
SELECT part, assembly_step
FROM parts_assembly
WHERE finish_date IS NULL;
```

#### 3. Tweet Histograms

Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket.

**Step 1**

```sql
SELECT 
  user_id, 
  COUNT(tweet_id) AS tweet_count_per_user 
FROM tweets 
WHERE tweet_date BETWEEN '2022-01-01' 
  AND '2022-12-31'
GROUP BY user_id;
```

**Step 2**

```sql
SELECT 
  tweet_count_per_user AS tweet_bucket, 
  COUNT(user_id) AS users_num 
FROM (
  SELECT 
    user_id, 
    COUNT(tweet_id) AS tweet_count_per_user 
  FROM tweets 
  WHERE tweet_date BETWEEN '2022-01-01' 
    AND '2022-12-31'
  GROUP BY user_id) AS total_tweets 
GROUP BY tweet_count_per_user;
```

**Approach II : Using CTE**

```sql
WITH total_tweets AS (
  SELECT 
    user_id, 
    COUNT(tweet_id) AS tweet_count_per_user
  FROM tweets 
  WHERE tweet_date BETWEEN '2022-01-01' 
    AND '2022-12-31' 
  GROUP BY user_id) 
  
SELECT 
  tweet_count_per_user AS tweet_bucket, 
  COUNT(user_id) AS users_num 
FROM total_tweets 
GROUP BY tweet_count_per_user;
```

#### 4. Laptop vs Mobile Viewership

Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

```sql
SELECT
    count(*) FILTER(WHERE device_type = "laptop") AS lapotp_views,
    count(*) FILTER(WHERE device_type IN('tablet','phone')) AS mobile_views
FROM viewership;
```

**Approach II : Sum and Case Statements**

```sql
SELECT 
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views, 
  SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_views 
FROM viewership;
```

#### 5. Data Science Skills

Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.

Write a query to list the candidates who possess all of the required skills for the job. Sort the output by candidate ID in ascending order.

```sql
SELECT candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id;
```

#### 6. Average Post Hiatus

Given a table of Facebook posts, for each user who posted at least twice in 2021, write a query to find the number of days between each user’s first post of the year and last post of the year in the year 2021. Output the user and number of the days between each user's first and last post.

```sql
SELECT 
    user_id,
    MAX(post_date::DATE) - MIN(post_date::DATE) AS days_between
FROM posts
WHERE DATE_PART('year',post_date::DATE) = 2021
GROUP BY user_id
HAVING count(post_id)>1;
```

#### 7. Teams Power Users

Write a query to identify the top 2 Power Users who sent the highest number of messages on Microsoft Teams in August 2022. Display the IDs of these 2 users along with the total number of messages they sent. Output the results in descending order based on the count of the messages.

```sql
select sender_id,
count(message_id) as count_messages
from messages
where extract(month from sent_date) = "8"
and extract(year from sent_date) = "2022"
group by sender_id
order by count_messages desc
limit 2;
```

#### 8. Duplicate Job Listings

Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings.

```sql
with job_count cte as(
    select 
        company_id,
        title,
        description,
        count(job_id) as job_count
    from job_listings
    group by company_id,title,description
)

SELECT COUNT(DISTINCT company_id) AS duplicate_companies
FROM job_count_cte
WHERE job_count > 1;
```

#### 9. Cities With Completed Trades

Assume you're given the tables containing completed trade orders and user details in a Robinhood trading system.

Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. Output the city name and the corresponding number of completed trade orders.

```sql
SELECT users.city,
COUNT(trades.order_id) AS total_orders
FROM trades
INNER JOIN users
ON trades.user_id = users.user_id
WHERE trades.status = "Completed"
GROUP BY users.city
ORDER BY total_orders DESC
```

#### 10. Average Review Ratings

Given the reviews table, write a query to retrieve the average star rating for each product, grouped by month. The output should display the month as a numerical value, product ID, and average star rating rounded to two decimal places. Sort the output first by month and then by product ID.

```sql
SELECT EXTRACT(MONTH from submit_date) AS mth,
product_id,
ROUND(AVG(stars),2) AS avg_stars
FROM reviews
GROUP BY 
EXTRACT(MONTH FROM submit_date), 
product_id
ORDER BY mth, product_id;
```

#### 11. App Click Through Rate

Assume you have an events table on Facebook app analytics. Write a query to calculate the click-through rate (CTR) for the app in 2022 and round the results to 2 decimal places.

Definition and note:

Percentage of click-through rate (CTR) = 100.0 * Number of clicks / Number of impressions

```sql
SELECT app_id,
ROUND(
100*SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END)/
SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END),2) AS ctr_rate

FROM events
WHERE timestamp >= '2022-01-01' 
  AND timestamp < '2023-01-01'
GROUP BY app_id;

```

#### 12. Second Day Confirmation

Assume you're given tables with information about TikTok user sign-ups and confirmations through email and text. New users on TikTok sign up using their email addresses, and upon sign-up, each user receives a text message confirmation to activate their account.

```sql
SELECT DISTINCT user_id
FROM emails
INNER JOIN texts
ON emails.email_id = texts.email_id
WHERE texts.action_date = emails.signup_date + INTERVAL '1 day'
AND texts.signup_action = "Confirmed";
```

#### 13. Card Issued Difference

Your team at JPMorgan Chase is soon launching a new credit card, and to gain some context, you are analyzing how many credit cards were issued each month.

Write a query that outputs the name of each credit card and the difference in issued amount between the month with the most cards issued, and the least cards issued. Order the results according to the biggest difference.

```sql
SELECT 
  card_name, 
  MAX(issued_amount) - MIN(issued_amount) AS difference
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY difference DESC;
```

#### 14. Compressed Mean

You're trying to find the mean number of items per order on Alibaba, rounded to 1 decimal place using tables which includes information on the count of items in each order (item_count table) and the corresponding number of orders for each item count (order_occurrences table).

```sql
SELECT 
  ROUND(
  SUM(item_count::DECIMAL*order_occurrences)
    /SUM(order_occurrences),1) AS mean
FROM items_per_order;
```

#### 15. Pharmacy Analytics Part 1

CVS Health is trying to better understand its pharmacy sales, and how well different products are selling. Each drug can only be produced by one manufacturer.

Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits. Display the result from the highest to the lowest total profit.

```sql
SELECT
  drug,
  total_sales - cogs AS total_profit
FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3;
```

#### 16. Pharmacy Analytics Part II

CVS Health is analyzing its pharmacy sales data, and how well different products are selling in the market. Each drug is exclusively manufactured by a single manufacturer.

Write a query to identify the manufacturers associated with the drugs that resulted in losses for CVS Health and calculate the total amount of losses incurred.

Output the manufacturer's name, the number of drugs associated with losses, and the total losses in absolute value. Display the results sorted in descending order with the highest losses displayed at the top.

```sql
SELECT
  manufacturer,
  COUNT(drug) AS drug_count, 
  SUM(cogs - total_sales) AS total_loss
FROM pharmacy_sales
WHERE cogs > total_sales
GROUP BY manufacturer
ORDER BY total_loss DESC;
```

#### 17. Pharmacy Analytics III

CVS Health is trying to better understand its pharmacy sales, and how well different products are selling.

Write a query to find the total drug sales for each manufacturer. Round your answer to the closest million, and report your results in descending order of total sales.

```sql
SELECT manufacturer,
CONCAT('$',ROUND(SUM(total_sales)/1000000,'million')) AS sales_mil
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC
```

#### 18. Patient Support Analytics Part I

UnitedHealth has a program called Advocate4Me, which allows members to call an advocate and receive support for their health care needs – whether that's behavioural, clinical, well-being, health care financing, benefits, claims or pharmacy help.

Write a query to find how many UHG members made 3 or more calls. case_id column uniquely identifies each call made.

```sql
SELECT COUNT(policy_holder_id) AS member_count
FROM (
      SELECT 
          policy_holder_id,
          COUNT(case_id)  AS call_count
      FROM callers
      GROUP BY policy_holder_id
      HAVING COUNT(case_id) >= 3
      ) AS call_records;
```

#### 19. Patient Support Analytics III

UnitedHealth Group has a program called Advocate4Me, which allows members to call an advocate and receive support for their health care needs – whether that's behavioural, clinical, well-being, health care financing, benefits, claims or pharmacy help.

Calls to the Advocate4Me call centre are categorised, but sometimes they can't fit neatly into a category. These uncategorised calls are labelled “n/a”, or are just empty (when a support agent enters nothing into the category field).

Write a query to find the percentage of calls that cannot be categorised. Round your answer to 1 decimal place.

```sql
SELECT
  ROUND(100.0 * COUNT(case_id) FILTER (
    WHERE call_category IS NULL OR call_category = 'n/a')
    / COUNT(case_id),1) AS uncategorised_call_pct
FROM callers;
```

#### 20. User's Third Transaction

Assume you are given the table below on Uber transactions made by users. Write a query to obtain the third transaction of every user. Output the user id, spend and transaction date.

```sql
SELECT user_id,spend,transaction_date
FROM (
  SELECT user_id, spend, transaction_date ROW_NUMBER() OVER (
      PARTITION BY user_id ORDER BY transaction_date
  ) AS row_number FROM transactions
) AS trans_no
WHERE row_number = 3;
```

[Row Number](https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-row_number-function/)

#### 21. Sending vs Opening Snaps

Assume you're given tables with information on Snapchat users, including their ages and time spent sending and opening snaps.

Write a query to obtain a breakdown of the time spent sending vs. opening snaps as a percentage of total time spent on these activities grouped by age group. Round the percentage to 2 decimal places in the output.

Notes:

Calculate the following percentages:
time spent sending / (Time spent sending + Time spent opening)
Time spent opening / (Time spent sending + Time spent opening)
To avoid integer division in percentages, multiply by 100.0 and not 100.

```sql
SELECT age.age_bucket,
    SUM(activities.time_spent) FILTER (WHERE activity_type = "send")/SUM(activities.time_spent)
    AS send_perc,
    SUM(activities.time_spend) FILTER(WHERE activity_type = "open")/SUM(activities.time_spent)
    AS open_perc
FROM activities 
INNER JOIN age_breakdown AS age ON activities.user_id = age.user_id 
WHERE activities.activity_type IN ('send', 'open') 
GROUP BY age.age_bucket;
```

#### 22. Tweet Rollling Averages

Given a table of tweet data over a specified time period, calculate the 3-day rolling average of tweets for each user. Output the user ID, tweet date, and rolling averages rounded to 2 decimal places.

```sql
SELECT    
  user_id,    
  tweet_date,   
  ROUND(AVG(tweet_count) OVER (
    PARTITION BY user_id     
    ORDER BY tweet_date     
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) -- take two rows before current row and the current row
  ,2) AS rolling_avg_3d
FROM tweets;
```

#### 23. International Call Percentage

Step 1: Join the tables to obtain the caller's and receiver's country information

To determine whether a call is international or not, we need country_id for both caller and receiver. This can be achieved by joining phone_info twice, first for the caller, and second for the receiver.

```sql
SELECT  
  caller.country_id AS caller_country,
  receiver.country_id AS receiver_country
FROM phone_calls AS calls
LEFT JOIN phone_info AS caller
  ON calls.caller_id = caller.caller_id
LEFT JOIN phone_info AS receiver
  ON calls.receiver_id = receiver.caller_id;
```

Step 2 : After obtaining the necessary info, we can start with the calculation. To do so, we need 2 metrics:

number of total calls
number of international calls
Getting the number of total calls is easy with COUNT(*).

```sql
SELECT 
  ROUND(
    100.0 * SUM(CASE WHEN caller.country_id <> receiver.country_id THEN 1 ELSE NULL END)
    /COUNT(*),1) AS international_call_pct
FROM phone_calls AS calls
LEFT JOIN phone_info AS caller
ON calls.caller_id = caller.caller_id
LEFT JOIN phone_info AS receiver
ON calls.receiver_id = receiver.caller_id;
```

