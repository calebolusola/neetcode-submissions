class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}

        for num in nums:
            hist[num] = hist.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in hist.items():
            buckets[freq].append(num)

        results = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results