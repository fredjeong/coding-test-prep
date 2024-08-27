#select year(b.sales_date) as year, month(b.sales_date) as month, count(*) as purchased_users, round(count(*) / (select count(*) from user_info where joined like '2021-%'), 1) as purchased_ratio
#from user_info a join online_sale b on a.user_id = b.user_id
#where date_format(a.joined, '%Y-%m') like '2021-%'
#group by date_format(b.sales_date, '%Y-%m')
#order by year asc, month asc

select year(b.sales_date) as year, month(b.sales_date) as month, count(distinct(a.user_id)) as purchased_users, round(count(distinct(a.user_id)) / (select count(*) from user_info where joined like '2021-%'), 1) as purchased_ratio
from user_info a join online_sale b on a.user_id = b.user_id
where a.joined like '2021-%'
group by year(b.sales_date), month(b.sales_date)
order by year asc, month asc