class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}

        # build the frequency histogram
        # [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5] -> {1:2, 2:3, 3:3, 4:1, 5:4}
        for num in nums:
            hist[num] = hist.get(num, 0) + 1

        # we store empty buckets for every index of every element in nums
        # because in the worst case scenario, every element in nums could be unique
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # we want to store a representation of every number that has a given frequency.
        # we use the positional index of a particular bucket in buckets as the frequency's representation.
        # then for every number that has frequency n, append that number to bucket n in buckets.
        for num, freq in hist.items():
            buckets[freq].append(num)

        # Return the top k most repeated numbers:
        results = []
        # we walk through the buckets backwards to get the highest frequencies
        # empty buckets at the end would be naturally skipped as they're empty
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results