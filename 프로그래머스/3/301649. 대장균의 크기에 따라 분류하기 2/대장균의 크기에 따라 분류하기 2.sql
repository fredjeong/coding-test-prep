select A.id,
case
    when A.percentile <= 0.25 then 'CRITICAL'
    when A.percentile <= 0.5 then 'HIGH'
    when A.percentile <= 0.75 then 'MEDIUM'
    else 'LOW'
end as colony_name
from (select id, percent_rank() over (order by size_of_colony desc) as percentile 
      from ecoli_data) as A
order by A.id