# https://leetcode.com/problems/top-travellers/

select u.name, sum(if(r.distance is null, 0, r.distance)) as travelled_distance 
from users u left join rides r on u.id = r.user_id
group by r.user_id 
order by travelled_distance desc, u.name;

# Runtime: 1876 ms, faster than 7.45% of MySQL online submissions for Top Travellers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Top Travellers.
