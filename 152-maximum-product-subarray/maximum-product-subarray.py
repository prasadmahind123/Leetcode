class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]

        for i in range(1 , len(nums)) :
            x = nums[i]
            
            if x < 0 :
                max_product , min_product = min_product , max_product 
                
            max_product = max(x , max_product * x)
            min_product = min(x , min_product * x)
            
            ans = max(ans , max_product)
        return ans