class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1 , len(nums)) :
            currSum = max(nums[i] , currSum + nums[i])
            maxSum = max(maxSum , currSum)

        return maxSum