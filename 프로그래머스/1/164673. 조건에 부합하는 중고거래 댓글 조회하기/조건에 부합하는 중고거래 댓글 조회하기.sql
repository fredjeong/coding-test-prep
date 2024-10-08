select A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, date_format(B.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD A 
join USED_GOODS_REPLY B on A.BOARD_ID = B.BOARD_ID
where A.CREATED_DATE like '2022-10-%'
order by B.CREATED_DATE asc, A.TITLE asc