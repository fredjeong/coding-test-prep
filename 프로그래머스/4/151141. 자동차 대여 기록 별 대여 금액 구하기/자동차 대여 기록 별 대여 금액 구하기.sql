select a.history_id, 
       (case when b.duration_type is null then round(a.daily_fee * a.period)
             else round(a.daily_fee * a.period * (100 - b.discount_rate)/100)
       end) as fee
from (select a.history_id, 
             case when datediff(a.end_date, a.start_date) + 1 < 7 then null 
                  when datediff(a.end_date, a.start_date) + 1 < 29 then "7일 이상" 
                  when datediff(a.end_date, a.start_date) + 1 < 89 then "30일 이상"
                  else "90일 이상"
             end as duration_type, 
             datediff(a.end_date, a.start_date) + 1 as period, 
             b.daily_fee,
             b.car_type
      from car_rental_company_rental_history a 
      join car_rental_company_car b 
      on a.car_id = b.car_id
      where b.car_type = '트럭') a 
      left join car_rental_company_discount_plan b 
      on a.duration_type = b.duration_type and a.car_type = b.car_type
order by fee desc, a.history_id desc