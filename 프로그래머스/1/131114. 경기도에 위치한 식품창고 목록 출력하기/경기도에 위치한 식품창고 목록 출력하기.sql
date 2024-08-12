select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') as FREEZER_YN # NULL 처리
from FOOD_WAREHOUSE
where ADDRESS like '경기도%' # 경기도에 위치한 창고. %가 있으면 '경기도'를 포함하는 행을 내보낸다.
order by WAREHOUSE_ID asc