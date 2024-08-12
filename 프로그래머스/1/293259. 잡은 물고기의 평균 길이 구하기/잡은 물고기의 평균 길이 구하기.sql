select round(sum(ifnull(LENGTH, 10)) / count(*), 2) as AVERAGE_LENGTH
from FISH_INFO