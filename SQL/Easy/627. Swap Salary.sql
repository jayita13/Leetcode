# https://leetcode.com/problems/swap-salary/

# update Salary
# set sex = case sex when 'm' then 'f'
# else 'm'
# end;

update Salary
set sex = if (sex = 'm', 'f', 'm');

# Runtime: 237 ms, faster than 75.13% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
