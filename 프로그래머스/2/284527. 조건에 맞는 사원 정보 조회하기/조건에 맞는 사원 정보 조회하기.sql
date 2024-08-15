select sum(score) as score, A.emp_no, A.emp_name, A.position, A.email
from hr_employees A join hr_grade B on A.emp_no = B.emp_no
group by year, emp_no
having B.year = '2022'
order by sum(score) desc
limit 1