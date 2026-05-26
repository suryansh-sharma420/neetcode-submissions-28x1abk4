class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix sum and suffix sum
        #brute force
        # n = len(nums)
        # res = [0] * n
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         product *= nums[j]
            
        #     res[i] = product 
        # return res

        #prefix is everything before i, suffix is after i
        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

        