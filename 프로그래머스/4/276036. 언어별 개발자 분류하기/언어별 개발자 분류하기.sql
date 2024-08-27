select *
from (select (case 
        when skill_code & (select code from skillcodes where name = 'Python') != 0 
         and 0 < any(select skill_code & code from skillcodes where category = 'Front End')
        then 'A' 
        when skill_code & (select code from skillcodes where name = 'C#') != 0 
        then 'B'
        when 0 < any(select skill_code & code from skillcodes where category = 'Front End')
        then 'C'
        end) as grade, id, email
      from developers) as temp
where grade is not null
order by grade asc, id asc