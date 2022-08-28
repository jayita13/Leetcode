# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

select customer_id, count(customer_id) as count_no_trans
from Visits v left join Transactions t 
on v.visit_id  = t.visit_id
where transaction_id is null
group by customer_id 

# Runtime: 2357 ms, faster than 18.89% of MySQL online submissions for Customer Who Visited but Did Not Make Any Transactions.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customer Who Visited but Did Not Make Any Transactions.
