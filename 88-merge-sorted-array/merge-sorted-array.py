class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = 0
        for i in range(m , len(nums1)) :
            
            if j < len(nums2) :
                nums1[i] = nums2[j]
                j += 1

        nums1.sort()
        