select a.category, sum(b.sales) as total_sales
from book a join book_sales b on a.book_id = b.book_id
where year(b.sales_date) = '2022' and month(b.sales_date) = '01'
group by a.category
order by a.category asc