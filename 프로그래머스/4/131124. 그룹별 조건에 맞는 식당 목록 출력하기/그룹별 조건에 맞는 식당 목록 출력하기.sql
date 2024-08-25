select a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
from member_profile a join rest_review b on a.member_id = b.member_id
where a.member_id in (select member_id#, counting
from(
select member_id, count(member_id) as counting
from rest_review
group by member_id
order by count(member_id) desc) as adsf
where counting in (select max(counting) as max_count
from (select count(member_id) as counting from rest_review group by member_id order by count(member_id) desc) as aefq))
order by b.review_date asc, b.review_text asc
##order by a.member_name
##group by a.member_name
#
##select member_id
##where member_id 
#


#select member_id#, counting
#from(
#select member_id, count(member_id) as counting
#from rest_review
#group by member_id
#order by count(member_id) desc) as adsf
#where counting in (select max(counting) as max_count
#from (select count(member_id) as counting from rest_review group by member_id order by count(member_id) desc) as aefq)


