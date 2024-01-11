class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range((2**n)):
            ans = []
            for j in range(n):
                if 1 << j & i:
                    ans.append(nums[j])
            res.append(ans)
        return res
