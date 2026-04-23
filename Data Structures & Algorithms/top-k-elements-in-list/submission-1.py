class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return list of elements
        #hashmap = defaultdict(list) #{class: [val]}
        freqmap = {}
        for i in range(len(nums)):
            freqmap[nums[i]] = freqmap.get(nums[i], 0) + 1

        #can i use lambda or a key to extract values and sort them?
        pairs = list(freqmap.items())
        pairs.sort(key = lambda p: p[1], reverse=True)
        return [p[0] for p in pairs[:k]]


