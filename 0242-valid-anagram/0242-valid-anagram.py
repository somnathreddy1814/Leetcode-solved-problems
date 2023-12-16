class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt=defaultdict(int)
        for x in s:
            cnt[x]+=1
        for x in t:
            cnt[x]-=1
        for val in cnt.values():
            if val!=0:
                return False
        return True

