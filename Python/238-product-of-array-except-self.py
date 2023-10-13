class Solution:
    def productExceptSelf_bruteforcee(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                answer[i] *= nums[j]

        return answer

    def productExceptSelf_optimal(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
