# Write your MySQL query statement below
select a.name as Customers
from Customers a
Left join Orders o
on a.id=o.customerId
where o.customerId IS Null;