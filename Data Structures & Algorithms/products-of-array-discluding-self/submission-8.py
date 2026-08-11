from itertools import accumulate
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # everything before it and everything after it
        prefix_products = list(accumulate(nums[:-1], mul))
        prefix_products = [1] + prefix_products
        
        suffix_products = list(accumulate(nums[:0:-1], mul))
        suffix_products.reverse()
        suffix_products += [1]

        results = []
        for prefix, suffix in zip(prefix_products, suffix_products):
            results.append(prefix*suffix)

        return results