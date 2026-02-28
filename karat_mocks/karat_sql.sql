-- You have a table user_logins with two columns: user_id (INT) and login_date (DATE). 
-- A user might log in every day, skip a few days, and log in again.

-- The Problem: Write a query to find the maximum number of consecutive days each user_id has logged in.
-- Hint: You cannot solve this with a simple COUNT or GROUP BY. You must use a specific
--  combination of Window Functions to group consecutive sequences.


---Approach: 
--  What are "Gaps and Islands"?
-- Imagine a user's login history on a calendar.

-- Islands: The days they logged in consecutively (e.g., Mon, Tue, Wed). These are unbroken streaks.

-- Gaps: The days they missed (e.g., Thu, Fri).

-- Our goal is to count how many days are in each "Island", and then find the biggest "Island" for each user.

-- 🪄 The Math Trick: Creating a Grouping Key
-- To use GROUP BY in SQL, all the rows in a streak need to share a common value. 
-- But right now, Jan 1st, Jan 2nd, and Jan 3rd are all different values. How do we force them to share a value?

-- We use two sequences that move at the exact same speed:

-- The Dates: Jan 1, Jan 2, Jan 3

-- A Row Number: 1, 2, 3

-- Because both sequences increment by exactly 1 at each step, if you subtract the Row Number from the Date,
--  the result will always be the exact same anchor date for that entire streak.

-- Let's look at User 1. If we subtract ROW_NUMBER (in days) from the login_date:

-- '2026-01-01' minus 1 day = '2025-12-31' (Island 1)

-- '2026-01-02' minus 2 days = '2025-12-31' (Island 1)

-- '2026-01-03' minus 3 days = '2025-12-31' (Island 1)

-- ...GAP in logins... User misses Jan 4th and 5th...

-- '2026-01-06' minus 4 days = '2026-01-02' (Island 2)

-- '2026-01-07' minus 5 days = '2026-01-02' (Island 2)

-- Notice how the math magically generated a shared identifier (2025-12-31 for the first streak, 
-- and 2026-01-02 for the second)? That synthetic date is the Island ID. Now we can easily GROUP BY it!


WITH DeduplicatedLogins AS (

    SELECT DISTINCT user_id, login_date
    FROM user_logins
),
IslandGenerator AS (
    -- Step 2: Apply the Math Trick.
    SELECT 
        user_id,
        login_date,

        login_date - (ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date)) * INTERVAL '1 day' AS island_id
    FROM DeduplicatedLogins
),

Streak_length as ( Select
   user_id, 
  island_id,
  COUNT(*) as consecutive_days
  from IslandGenerator
  Group by user_id, island_id
  
  )
  
 Select user_id , MAX(consecutive_days) from Streak_length
 group by user_id  order by user_id
