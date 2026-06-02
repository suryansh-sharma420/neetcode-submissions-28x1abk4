class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #no duplicates, triplets that sum to 0
        nums.sort()
        res = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            current = nums[i]

            while left < right:
                total = current + nums[left] + nums[right]
                if total == 0:
                    if [current, nums[left], nums[right]] not in res:
                        res.append([current, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res