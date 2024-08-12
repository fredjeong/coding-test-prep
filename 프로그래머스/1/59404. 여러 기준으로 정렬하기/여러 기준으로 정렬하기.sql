select ANIMAL_ID, NAME, DATETIME # 아이디, 이름, 보호 시작일 조회
from ANIMAL_INS # 테이블 선택
order by NAME asc, DATETIME desc # 이름 순으로 조회, 동일한 이름이면 DATETIME이 큰 (나중에 시작한) 동물 우선