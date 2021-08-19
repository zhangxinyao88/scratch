class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            imple = target - nums[i]
            if imple in dic:
                return [dic.get(imple), i]
            dic[nums[i]] = i
