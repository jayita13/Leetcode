# https://leetcode.com/problems/customers-who-never-order/

# Write your MySQL query statement below
select name as 'Customers'
from Customers
where id not in (select customerId from orders)

# Success Details 
# Runtime: 505 ms, faster than 71.09% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
