select count(*) as fish_count
from fish_info A join fish_name_info B on A.fish_type = B.fish_type
where B.fish_name in ('BASS', 'SNAPPER')