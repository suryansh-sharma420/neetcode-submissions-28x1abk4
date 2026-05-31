class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #should be one greater
        #handle duplicates - hashmap
        #a number which does not have a n-1 in the set - start of a sequence 
        seq = 0
        longest = 0
        seenset = set(nums)
        
        for n in seenset:
            if not n-1 in seenset:
                length = 1
                while n + length in seenset:
                    length += 1
                longest = max(longest, length)
        
        return longest
























        if not nums:
            return 0
        nums.sort()

        res = 0
        curr = nums[0] 
        streak = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i] #curr points to nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1 
            streak += 1
            curr += 1
            res = max(res, streak)
        return res