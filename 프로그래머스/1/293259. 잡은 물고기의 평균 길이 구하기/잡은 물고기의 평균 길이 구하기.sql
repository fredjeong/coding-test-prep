select round(sum(ifnull(length, 10)) / count(*), 2) as average_length
from fish_info