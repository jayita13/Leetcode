# https://leetcode.com/problems/bank-account-summary-ii/

select name, sum(amount) as balance from Users u 
inner join Transactions t 
on u.account = t.account 
group by t.account
having balance > 10000;

# Runtime: 655 ms, faster than 73.58% of MySQL online submissions for Bank Account Summary II.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Bank Account Summary II.
