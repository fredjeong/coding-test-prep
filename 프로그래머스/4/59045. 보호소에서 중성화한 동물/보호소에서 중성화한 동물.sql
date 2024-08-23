select animal_id, animal_type, name
from animal_ins
where (animal_id in (select animal_id from animal_outs where sex_upon_outcome like 'Spayed%' or sex_upon_outcome like 'Neutered%')) and sex_upon_intake like "Intact%"

#select a.animal_id, a.animal_type, a.name
#from animal_ins a join animal_outs b on a.animal_id = b.animal_id
#where a.sex_upon_intake != b.sex_upon_outcome
#order by a.animal_id asc