class Solution:
    def hIndex_brute_force(self, citations: list[int]) -> int:
        """
        Brute Force
        TC: O(n^2), SC: O(1) where n = len(citations)
        """
        number_of_papers = len(citations)
        max_h = 0

        def is_cited_at_least_h_times(h):
            count = 0
            for citation in citations:
                if citation >= h:
                    count += 1

            return count >= h

        for h in range(number_of_papers):
            if is_cited_at_least_h_times(h):
                max_h = h

        return max_h

    def hIndex_binary_search(self, citations: list[int]) -> int:
        """
        Binary Search
        TC: O(nlogn), SC: O(1) where n = len(citations)
        """
        max_h = 0

        def is_cited_at_least_h_times(h):
            count = 0
            for citation in citations:
                if citation >= h:
                    count += 1

            return count >= h

        left = 0
        right = len(citations)

        while left <= right:
            h = left + (right - left) // 2

            if is_cited_at_least_h_times(h):
                max_h = h
                left = h + 1
            else:
                right = h - 1

        return max_h

    def hIndex(self, citations: list[int]) -> int:
        """
        Bucket Sort
        TC: O(n), SC: O(n) where n = len(citations)
        """
        number_of_papers = len(citations)
        citation_counts = [0] * (number_of_papers + 1)

        for citation in citations:
            if citation >= number_of_papers:
                citation_counts[-1] += 1
            else:
                citation_counts[citation] += 1

        max_h = 0

        for citation in range(number_of_papers, -1, -1):
            max_h += citation_counts[citation]

            if max_h >= citation:
                return citation

        return max_h
