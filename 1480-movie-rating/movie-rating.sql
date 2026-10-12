/* Write your PL/SQL query statement below */
with res as (
    select user_id , count(*) as cnt 
    from MovieRating
    group by user_id
),
ans as (
    select movie_id , 
    avg(rating) as avg_rating
    from MovieRating
    WHERE created_at >= DATE '2020-02-01'
    AND created_at <  DATE '2020-03-01'
    group by movie_id 
)
select distinct first_value(u.name) over(
    ORDER BY cnt DESC, u.name ASC
)as results
from Users u
join res r
on u.user_id = r.user_id

union all

select distinct  first_value(m.title) over(
    ORDER BY a.avg_rating DESC, m.title ASC
) as results
from Movies m
join ans a 
on m.movie_id = a.movie_id;

