# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)

        freq = list(freq_map.values())
        freq.sort()

        remain = 0

        for i in range(len(freq)):
            remain += freq[i]

            if remain > k :
                return len(freq) - i
        
        return 0
