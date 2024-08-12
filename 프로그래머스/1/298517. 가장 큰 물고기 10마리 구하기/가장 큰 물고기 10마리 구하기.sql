select ID, ifnull(LENGTH, 10) as LENGTH
from FISH_INFO
order by LENGTH desc, ID asc
limit 10