class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 2, 3]
        # [3, 2, 3]
        encountered = {}
        for idx, i in enumerate(nums):
            encountered[idx] = i

        for index, value in encountered.items():
            diff = target - value

            # if diff in encountered.values():
            #     return [index, next(k for k, v in encountered.items() if v == diff and k != i)]

            if diff in encountered.values():
                other = next(
                    (
                        k
                        for k, v in encountered.items()
                        if v == diff and k != index
                    ),
                    None,
                )

                if other is not None:
                    return [index, other]
        return []
