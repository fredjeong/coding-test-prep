select A.item_id, A.item_name
from item_info A join item_tree B on A.item_id = B.item_id
where B.parent_item_id is null
order by A.item_id asc
