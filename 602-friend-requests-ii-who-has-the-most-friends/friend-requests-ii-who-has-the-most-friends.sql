/* Write your PL/SQL query statement below */
with accepts as (
    select requester_id as id 
    from RequestAccepted 

    union all

    select accepter_id as id 
    from RequestAccepted 

)
select  * 
from (
    select id , count(*) as num
    from accepts
    group by id
    order by count(*) desc
)
where ROWNUM = 1;