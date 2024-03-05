-- my sol
select t1.user_id,
    case
    when t2.action is null then 0
    else round(t2.cr/t1.total, 2)
    end as confirmation_rate
 from
(select s.user_id, c.action,
case
    when c.action is null then 0
    else count(*)
    end as total
 from Signups s left join Confirmations c on s.user_id = c.user_id group by s.user_id) t1
 left join
(select s.user_id, c.action, Count(*) as cr from Signups s left join Confirmations c on s.user_id = c.user_id where c.action = "confirmed"  group by s.user_id, c.action) t2
on t1.user_id = t2.user_id

-- opt
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by s.user_id;

