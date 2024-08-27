#select a.history_id, 
#       (case when b.duration_type is null then round(a.daily_fee * a.period)
#             else round(a.daily_fee * a.period * (100 - b.discount_rate)/100)
#       end) as fee #, a.daily_fee, a.period, b.discount_rate
#from (select a.history_id, 
#       case when datediff(a.end_date, a.start_date) + 1 < 7 then null 
#            when datediff(a.end_date, a.start_date) + 1 < 29 then "7일 이상" 
#            when datediff(a.end_date, a.start_date) + 1 < 89 then "30일 이상"
#            else "90일 이상"
#       end as duration_type, 
#       datediff(a.end_date, a.start_date) + 1 as period, 
#       b.daily_fee
#from car_rental_company_rental_history a join car_rental_company_car b on a.car_id = b.car_id
#where b.car_type = '트럭') a left join car_rental_company_discount_plan b on a.duration_type = b.duration_type
#group by a.history_id
#order by fee desc, a.history_id desc


SELECT  D.HISTORY_ID
        , ROUND(IF(D.DISCOUNT_RATE IS NULL, D.DAILY_FEE * D.DATE_DIFF, D.DAILY_FEE * D.DATE_DIFF * (100-D.DISCOUNT_RATE)*0.01),0) AS FEE
  FROM  (
        SELECT  A.*
                , B.HISTORY_ID
                , DATEDIFF(B.END_DATE,B.START_DATE) + 1 AS DATE_DIFF
                , C.DISCOUNT_RATE
          FROM  CAR_RENTAL_COMPANY_CAR A
          LEFT
          JOIN  CAR_RENTAL_COMPANY_RENTAL_HISTORY B
            ON  A.CAR_ID = B.CAR_ID
          LEFT
          JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
            ON  CASE WHEN DATEDIFF(B.END_DATE,B.START_DATE) BETWEEN 7 AND 29 THEN C.PLAN_ID = 10
                     WHEN DATEDIFF(B.END_DATE,B.START_DATE) BETWEEN 30 AND 89 THEN C.PLAN_ID = 11
                     WHEN DATEDIFF(B.END_DATE,B.START_DATE) >= 90 THEN C.PLAN_ID = 12 END
         WHERE  A.CAR_TYPE = '트럭'
         ) D 
 ORDER
    BY   FEE DESC 
         , HISTORY_ID DESC