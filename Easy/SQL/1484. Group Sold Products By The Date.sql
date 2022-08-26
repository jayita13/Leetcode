# https://leetcode.com/problems/group-sold-products-by-the-date/

select sell_date, count(distinct product) num_sold, 
group_concat(distinct product) products
from Activities
group by sell_date 

# Runtime: 542 ms, faster than 50.66% of MySQL online submissions for Group Sold Products By The Date.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Group Sold Products By The Date.
