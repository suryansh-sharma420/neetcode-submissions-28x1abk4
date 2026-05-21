class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return list of elements
        #hashmap = defaultdict(list) #{class: [val]}
        #use key and lambda
        #bucket sort - 
        res = []
        buckets = [[] for i in range(len(nums)+1)] #stores val in index where index=freq
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        

        for key, frequency in freq.items():
            buckets[frequency].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res



        # freqmap = {}
        # for i in range(len(nums)):
        #     freqmap[nums[i]] = freqmap.get(nums[i], 0) + 1

        # #can i use lambda or a key to extract values and sort them?
        # pairs = list(freqmap.items())
        # pairs.sort(key = lambda p: p[1], reverse=True)
        # return [p[0] for p in pairs[:k]]


