from typing import List


class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


class TimeOptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i

        return []


class SpaceOptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indexes = [(num, i) for i, num in enumerate(nums)]
        nums_with_indexes.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            sum = nums_with_indexes[l][0] + nums_with_indexes[r][0]
            if sum == target:
                return [nums_with_indexes[l][1], nums_with_indexes[r][1]]
            elif sum < target:
                l += 1
            else:
                r -= 1

        return []


class Solution(SpaceOptimizedSolution):
    pass
