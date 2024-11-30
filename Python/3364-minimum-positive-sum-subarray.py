class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float("inf")

        for size in range(l, r + 1):
            for right in range(size - 1, len(nums)):
                cur_sum = sum(nums[right - size + 1 : right + 1])

                if cur_sum > 0:
                    min_sum = min(min_sum, cur_sum)

        return min_sum if min_sum != float("inf") else -1
