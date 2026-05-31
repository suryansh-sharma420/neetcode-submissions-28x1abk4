class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #cant be equal
        #1 indexed

        hashmap = {}
        for idx, val in enumerate(numbers):
            complement = target - val
            if complement in hashmap.keys() and complement != val:
                return [hashmap[complement] + 1, idx + 1]
            
            hashmap[val] = idx 
        return []