select a.id, coalesce(b.count, 0) as child_count
from ecoli_data a left join (select parent_id, count(*) as count from ecoli_data group by parent_id having parent_id is not null) b on a.id = b.parent_id
order by a.id asc