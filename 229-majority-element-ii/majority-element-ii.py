class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        res = []
        n = len(nums) // 3
        for key , val in count.items() :
            if val >  n :
                res.append(key)

        return res