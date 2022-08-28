# https://leetcode.com/problems/rearrange-products-table/

Select product_id, "store1" as store, store1 as price from Products where store1 is not null
union
Select product_id, "store2" as store, store2 as price from Products where store2 is not null
union
Select product_id, "store3" as store, store3 as price from Products where store3 is not null;

# Runtime: 418 ms, faster than 96.85% of MySQL online submissions for Rearrange Products Table.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rearrange Products Table.
