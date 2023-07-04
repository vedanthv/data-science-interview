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

