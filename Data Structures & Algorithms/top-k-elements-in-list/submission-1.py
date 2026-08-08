class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}

        # build the frequency histogram
        # [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5] -> {1:2, 2:3, 3:3, 4:1, 5:4}
        for num in nums:
            hist[num] = hist.get(num, 0) + 1
        
        # we want to store each frequency and how many numbers have that frequency
        # if we use a dict comprehension here, we would lose numbers that happen to have the same frequency

        # this stores: "Question: which number appears x times? A: y - for every frequency"
        freq_reps = [(value, key) for key, value in hist.items()] # -> [(2, 1), (3, 2), (3, 3), (1, 4), (5, 5)]

        # we use .sort because, by default, it sorts lists of tuples by the first element in each tuple
        freq_reps.sort(reverse=True) # -> [(5, 5), (3, 2), (3, 3), (2, 1), (1, 4)]

        # Return the top k most repeated numbers:
        results = []
        for _, num in freq_reps:
            results.append(num)
            if len(results) == k:
                break

        return results