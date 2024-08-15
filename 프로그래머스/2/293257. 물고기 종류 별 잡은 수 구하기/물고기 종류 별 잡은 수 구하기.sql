select count(*) as fish_count, B.fish_name
from fish_info A join fish_name_info B on A.fish_type = B.fish_type
group by B.fish_name
order by fish_count desc