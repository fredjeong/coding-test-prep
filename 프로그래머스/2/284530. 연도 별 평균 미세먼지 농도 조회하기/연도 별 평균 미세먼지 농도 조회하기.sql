select (year(YM)) as year, (round(sum(pm_val1)/count(pm_val1), 2)) as 'pm10', (round(sum(pm_val2)/count(pm_val2), 2)) as 'pm2.5'
from air_pollution
where location2 like '수원'
group by year(YM)
order by year asc