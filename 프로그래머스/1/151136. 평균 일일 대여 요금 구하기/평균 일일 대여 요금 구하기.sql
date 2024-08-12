select round(sum(DAILY_FEE) / count(CAR_TYPE)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV'