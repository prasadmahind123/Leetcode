class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zero = 0
        one = 0
        two = 0

        for n in nums :
            if n == 0 :
                zero += 1
            elif n == 1 :
                one += 1
            else :
                two += 1

        i = 0

        while zero > 0 :
            nums[i] = 0
            i += 1 
            zero -= 1

        while one > 0 :
            nums[i] = 1
            i += 1
            one -= 1

        while two > 0 :
            nums[i] = 2
            i += 1
            two -= 1

        
        