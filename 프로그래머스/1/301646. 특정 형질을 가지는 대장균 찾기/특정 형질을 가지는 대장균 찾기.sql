select count(*) as COUNT
from ECOLI_DATA
where conv(GENOTYPE, 10, 2) not like '%1_' and (conv(GENOTYPE, 10, 2) like '%1' or conv(GENOTYPE, 10, 2) like '%1__')