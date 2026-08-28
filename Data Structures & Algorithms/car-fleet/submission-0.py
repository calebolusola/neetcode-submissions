class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [4,1,0,7]
        # speed = [2,2,1,1]
        # target = 10
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # reversed sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)