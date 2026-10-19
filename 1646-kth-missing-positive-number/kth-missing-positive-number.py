class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        count = 0
        i = 1

        while True :
            if count == k :
                return i - 1
                break
            
            if i not in arr :
                count += 1
                i += 1
            else :
                i+= 1