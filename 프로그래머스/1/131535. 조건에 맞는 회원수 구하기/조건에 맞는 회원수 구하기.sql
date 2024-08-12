select count(*) as USERS
from USER_INFO
where year(JOINED) = 2021 AND AGE >= 20 AND AGE <= 29
