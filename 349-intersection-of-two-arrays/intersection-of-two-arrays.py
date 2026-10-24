class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = Counter(nums1)
        res = set()
        
        for num in nums2:
            if counts[num] > 0:
                res.add(num)
                counts[num] -= 1
                
        return list(res)