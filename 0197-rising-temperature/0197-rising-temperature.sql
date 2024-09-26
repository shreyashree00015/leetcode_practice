# Write your MySQL query statement below
select a.id as Id
from Weather a
join Weather p
on a.recordDate = Date_Add(p.recordDate, INTERVAL 1 Day)
where a.temperature > p.temperature;
