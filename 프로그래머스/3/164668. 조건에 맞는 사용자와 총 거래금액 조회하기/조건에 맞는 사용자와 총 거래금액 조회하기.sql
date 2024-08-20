select b.user_id, b.nickname, sum(a.price) as total_sales
from used_goods_board a join used_goods_user b on a.writer_id = b.user_id
where a.status = 'DONE'
# where 절은 모든 행에 대해 조건을 건다
group by a.writer_id
having total_sales >= 700000
# having 절은 group에 조건을 적용한다
order by total_sales asc