class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        select min and swap

        brute: count all 3, then replace the array with the 3
        """
        c0 = 0
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            else:
                c2 += 1
        
        for i in range(c0):
            nums[i] = 0 
        for i in range(c0, c0 + c1):
            nums[i] = 1
        for i in range(c0 + c1, c0 + c1 + c2):
            nums[i] = 2
        
        