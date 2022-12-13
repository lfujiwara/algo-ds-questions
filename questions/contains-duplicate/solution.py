from typing import List


class NaiveSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Straightforward O(n^2) time, O(1) space
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True


class ALittleBitBetterSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n log n) time (creating set takes n log n), O(n) space (set is allocated in memory)
        """
        return len(nums) != len(set(nums))


class SpaceOptimizedSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n log n) time (sorting takes n log n), O(1) space (sorting is done in place)
        make sure you are allowed to modify the input
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


class TimeOptimizedSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n log n) time (sorting takes n log n), O(1) space (sorting is done in place)
        make sure you are allowed to modify the input
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class Solution(TimeOptimizedSolution):
    pass
