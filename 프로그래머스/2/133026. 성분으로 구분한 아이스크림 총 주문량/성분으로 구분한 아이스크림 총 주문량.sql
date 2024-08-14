select B.ingredient_type, sum(A.total_order) as total_order
from first_half A join icecream_info B on A.flavor = B.flavor
group by B.ingredient_type
order by total_order asc