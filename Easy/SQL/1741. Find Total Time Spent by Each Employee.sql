# https://leetcode.com/problems/find-total-time-spent-by-each-employee/

# Write your MySQL query statement below
Select event_day as day, emp_id, sum(out_time - in_time) as total_time
from Employees
where in_time < out_time and 
in_time > 0 and out_time <= 1440
group by emp_id, event_day

# Runtime: 506 ms, faster than 72.76% of MySQL online submissions for Find Total Time Spent by Each Employee.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Find Total Time Spent by Each Employee.
