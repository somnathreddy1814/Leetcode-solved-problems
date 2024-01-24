class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        ans=[]
        def CombHelper(ind,target):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                CombHelper(ind,target-candidates[ind])
                ds.pop()
            CombHelper(ind+1,target)
        CombHelper(0,target)
        return ans
                