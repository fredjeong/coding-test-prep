-- 코드를 입력하세요
select ANIMAL_ID, NAME # 아이디와 이름 조회
from ANIMAL_INS # 데이터 호출
where  INTAKE_CONDITION != 'Aged'# 조건 확인
order by ANIMAL_ID asc # 아이디 순 (오름차순) 정렬