# https://leetcode.com/problems/duplicate-emails/

select email from person
group by email having count(email) >1

# Runtime: 642 ms, faster than 22.44% of MySQL online submissions for Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
