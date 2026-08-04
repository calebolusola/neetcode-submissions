class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # "bbcc"
        # "ccbc"

        unique_s = set(s)
        unique_t = set(t)
        if (
            # check if they have the same absolute length
            len(s) == len(t)

            # check if they have the same number of distinct characters
            and unique_s == unique_t

            # check if the sum of their ASCII values equal eachother
            # (this can fail if the other set happens to have a combination
            # of letters whose ASCII values add up to match those of
            # the other set even though they are different)
            and sum(ord(i) for i in s) == sum(ord(j) for j in t)
        ):
            # count how many times the unique letters in "a" appear in "a" versus in "b"
            for i in unique_s:
                if s.count(i) != t.count(i):
                    return False
            # if they have the same character frequency, return true after all the other checks have passed
            return True
        return False
