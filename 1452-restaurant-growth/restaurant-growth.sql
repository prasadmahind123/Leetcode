with total as (
    select visited_on , sum(amount) as daily_total
    from Customer
    group by visited_on
),
running_avg as (
    select visited_on , 
    sum(daily_total) over(
        order by visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as amount ,
    ROUND(sum(daily_total) over(
        order by visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) / 7, 2)as average_amount
    from total
)
select TO_CHAR(visited_on , 'YYYY-MM-DD') as visited_on , amount , average_amount
from (
    select t.* , ROWNUM rnum
    from (
        select * from running_avg
        order by visited_on
    ) t
)
where rnum > 6
order by visited_on;
