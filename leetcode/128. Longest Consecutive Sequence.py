# way 1 - put list into a set, and look for consecutives and remove from the set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        theset = set(nums)

        for num in nums:
            if num not in theset:
                continue
            curr = 1
            left = right = num
            theset.discard(num)
            while left - 1 in theset:
                curr += 1
                left -= 1
                theset.discard(left)
            while right + 1 in theset:
                curr += 1
                right += 1
                theset.discard(right)
            res = max(res, curr)

        return res


# way 2 - check the set, if no numbers in the set less than it, add 1 by 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        theset = set(nums)
        res = 0
        for num in theset:
            if num - 1 not in theset:
                y = num + 1
                while y in theset:
                    y += 1
                res = max(res, y - num)

        return res
