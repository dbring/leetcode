class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        TC: O(nlogn), SC:O(n) where n = len(names)
        """
        return [
            name
            for name, _ in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        ]
