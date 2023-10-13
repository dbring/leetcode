from collections import defaultdict
import heapq
import random


class Solution:
    def get_counts(self, nums):
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return counts

    def topKFrequent_quickselect(self, nums, k):
        count = self.get_counts(nums)
        unique = list(count.keys())

        def swap(i, j):
            unique[i], unique[j] = unique[j] = unique[i]

        def quickselect(left, right, k_smallest):
            """
            Sorts the unique array from smallest count to largest count
            """
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_count = count[unique[pivot_index]]
            swap(pivot_index, right)

            partition_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_count:
                    swap(partition_index, i)
                    partition_index += 1

            swap(right, partition_index)
            pivot_index = partition_index

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k :]

    def topKFrequent_bucketsort(self, nums: list[int], k: int) -> list[int]:
        """
        Bucket Sort
        TC: O(n) S:O(n)
        """
        counts = self.get_counts(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        top_k_frequent_nums = []

        for num, count in counts.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k_frequent_nums.append(num)
                if len(top_k_frequent_nums) == k:
                    return top_k_frequent_nums

        return top_k_frequent_nums

    def topKFrequent_heap(self, nums: list[int], k: int) -> list[int]:
        """
        Min Heap
        TC: O(nlogk) SC: O(n), n = len(nums)
        """
        counts = self.get_counts(nums)
        min_heap = []
        top_k_frequent_nums = []

        for num, count in counts.items():
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        while min_heap:
            _, num = heapq.heappop(min_heap)
            top_k_frequent_nums.append(num)

        return top_k_frequent_nums

    def topKFrequent_sort(self, nums: list[int], k: int) -> list[int]:
        """
        Sorting
        https://leetcode.com/problems/top-k-frequent-elements/description/
        TC: O(nlogn) SC:O(n), n = len(nums)
        """
        counts = self.get_counts(nums)
        top_k_tuples = list(counts.items())
        top_k_frequent_nums = []

        top_k_tuples.sort(key=lambda x: -x[1])

        for num, _ in top_k_tuples:
            top_k_frequent_nums.append(num)
            k -= 1
            if k == 0:
                break

        return top_k_frequent_nums
