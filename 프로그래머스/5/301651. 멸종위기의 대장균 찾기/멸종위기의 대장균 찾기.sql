with recursive temp as (select id, parent_id, 1 as generation
                        from ecoli_data
                        where parent_id is null
                        union all
                        select a.id, a.parent_id, b.generation + 1
                        from temp b join ecoli_data a on b.id = a.parent_id)

select count(*) count, generation
from temp
where id not in (select distinct(parent_id)
                 from temp
                 where parent_id is not null)
group by generation
order by generation