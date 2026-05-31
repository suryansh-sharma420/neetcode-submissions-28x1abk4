class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #cant be equal
        #1 indexed
        #sorted array and one valid solution
        left = 0
        n = len(numbers)
        right = n-1

        while left < right:
            add = numbers[left] + numbers[right]
            if add == target:
                return [left+1, right+1]
            elif add < target:
                left += 1
            else:
                right -= 1
        return 






        # hashmap = {}
        # for idx, val in enumerate(numbers):
        #     complement = target - val
        #     if complement in hashmap.keys() and complement != val:
        #         return [hashmap[complement] + 1, idx + 1]
            
        #     hashmap[val] = idx 
        # return []