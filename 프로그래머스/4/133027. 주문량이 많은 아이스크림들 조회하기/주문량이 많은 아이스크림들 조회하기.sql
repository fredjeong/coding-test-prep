select flavor
from (select *
from first_half 
union all
select *
from july) as united
group by flavor
order by sum(total_order) desc
limit 3