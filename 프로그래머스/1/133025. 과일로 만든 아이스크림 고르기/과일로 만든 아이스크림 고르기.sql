select A.FLAVOR
from FIRST_HALF A 
join ICECREAM_INFO B on A.FLAVOR = B.FLAVOR # 각각의 열에 해당하는 조건을 출력하기 위해 두 테이블을 연결 (join)
where A.TOTAL_ORDER >= 3000 and B.INGREDIENT_TYPE = 'fruit_based'
order by A.TOTAL_ORDER desc