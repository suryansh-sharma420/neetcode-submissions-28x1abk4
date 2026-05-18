class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        select min and swap

        brute: count all 3, then replace the array with the 3
        optimal: have 2 pointers, and a 3rd pointer to iterate through a while loop
        1. mid ptr cannot exceed high ptr
        2. if mid = 0, swap with low, inc low and mid
        3. if mid = 2, swap with high, dec high, but dont increment mid(edge case)
        4. if mid = 1, just increment mid
        """

        low = 0 
        mid = 0 
        high = len(nums) - 1 

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        












        # c0 = 0
        # c1 = 0
        # c2 = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         c0 += 1
        #     elif nums[i] == 1:
        #         c1 += 1
        #     else:
        #         c2 += 1
        
        # for i in range(c0):
        #     nums[i] = 0 
        # for i in range(c0, c0 + c1):
        #     nums[i] = 1
        # for i in range(c0 + c1, c0 + c1 + c2):
        #     nums[i] = 2
        
        