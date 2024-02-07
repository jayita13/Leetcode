# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_elements = heapq.nlargest(k, count, key=count.get)
        return top_elements

  """ Runtime 98 ms Beats 35.51% of users with Python3
Memory 20.76 MB Beats 98.57% of users with Python3 """
