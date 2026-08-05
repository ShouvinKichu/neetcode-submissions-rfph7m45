class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for n in nums:
            if n in countMap:
                return True
            countMap[n] = 1
        return False

        