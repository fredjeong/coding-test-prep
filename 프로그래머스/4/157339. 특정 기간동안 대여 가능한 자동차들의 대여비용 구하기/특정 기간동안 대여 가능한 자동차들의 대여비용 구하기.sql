select a.car_id, a.car_type, round(a.daily_fee * 30 * (100 - b.discount_rate) / 100) as fee
from (select a.car_id, a.car_type, a.daily_fee
      from car_rental_company_car a 
      join car_rental_company_rental_history b 
      on a.car_id = b.car_id
      where a.car_id not in (select a.car_id
                             from car_rental_company_car a 
                             join car_rental_company_rental_history b 
                             on a.car_id = b.car_id
                             where '2022-11' 
                             between date_format(b.start_date, '%Y-%m-%d') 
                             and date_format(b.end_date, '%Y-%m-%d')
                             group by a.car_id)
      group by a.car_id) a 
      join (select car_type, discount_rate
            from car_rental_company_discount_plan
            where duration_type = '30일 이상' and (car_type = '세단' or car_type = 'SUV')) b
      on a.car_type = b.car_type
where round(a.daily_fee * 30 * (100 - b.discount_rate) / 100) < 2000000 and round(a.daily_fee * 30 * (100 - b.discount_rate) / 100) >= 500000
#where round(a.daily_fee * 30 * (100 - b.discount_rate) / 100) >= 500000 and round(a.daily_fee * 30 * (100 - b.discount_rate) / 100) * 30 < 2000000
order by fee desc, car_type asc, car_id desc