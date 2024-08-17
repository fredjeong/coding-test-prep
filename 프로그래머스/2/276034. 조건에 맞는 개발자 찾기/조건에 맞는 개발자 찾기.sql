select id, email, first_name, last_name from developers
where skill_code & (select code
                   from skillcodes
                   where name = 'Python')
or skill_code & (select code
                from skillcodes
                where name = 'C#')
order by id

# 자리 수를 표시해야 한다