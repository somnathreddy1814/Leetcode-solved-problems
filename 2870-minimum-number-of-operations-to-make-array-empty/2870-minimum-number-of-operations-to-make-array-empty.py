class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums).values()
        return -1 if 1 in count else sum((c + 2) // 3 for c in count)
