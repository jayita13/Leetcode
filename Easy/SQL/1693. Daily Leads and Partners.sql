# https://leetcode.com/problems/daily-leads-and-partners/

Select date_id, make_name, count(distinct(lead_id)) as unique_leads, 
count(distinct(partner_id)) as unique_partners 
from DailySales
group by date_id, make_name;

# Runtime: 1217 ms, faster than 12.37% of MySQL online submissions for Daily Leads and Partners.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Daily Leads and Partners.
