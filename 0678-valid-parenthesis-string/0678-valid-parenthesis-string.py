class Solution:
    def checkValidString(self, s: str) -> bool:
        cntmin=0
        cntmax=0
        for i in range(len(s)):
            if s[i]=='(':
                cntmin+=1
                cntmax+=1
            if s[i]==')':
                cntmin-=1
                cntmax-=1
            if s[i]=='*':
                cntmin-=1
                cntmax+=1
            if cntmin<0:
                cntmin=0
            if cntmax<0:
                return False
            if i==len(s)-1:
                if cntmin==0:
                    return True
        