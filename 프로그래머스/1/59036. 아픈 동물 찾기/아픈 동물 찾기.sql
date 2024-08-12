-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME # 아이디와 이름을 조회
from ANIMAL_INS # 주어진 데이터 호출
where INTAKE_CONDITION like 'sick' # 아픈 동물인지 확인
order by ANIMAL_ID asc; # ID 오름차순으로 정렬