--My solution
select e.name from Employee e left join (SELECT managerId as idd
FROM employee
GROUP BY managerId
HAVING COUNT(*) >= 5)  ee on True where e.id = ee.idd

--Opt solution
select name from employee where id in (select managerId from employee group by managerId having count(managerId)>4);