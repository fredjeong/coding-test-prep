# itme_info와 item_tree를 합친 테이블에서
# item_tree의 행 중에서
# parent_item_id의 rarity가 'rare'인 행들 정렬

select a.item_id, a.item_name, a.rarity
from item_info a join item_tree b on a.item_id = b.item_id
where b.parent_item_id in (select item_id
                          from item_info
                          where rarity = 'rare')
order by a.item_id desc
