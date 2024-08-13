# if 사용해서 풀기

#select animal_id, name, if(sex_upon_intake like 'neutered%' or sex_upon_intake like 'spayed%', 'O', 'X') as '중성화'
#from animal_ins
#order by animal_id

# case 사용해서 풀기

select animal_id, name, case when (sex_upon_intake like 'neutered%' or sex_upon_intake like 'spayed%') then 'O' else 'X' end as '중성화'
from animal_ins
order by animal_id