class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[1])
        ans=0
        arrow=0
        for [start,end] in points:
            if ans==0 or start>arrow:
                arrow=end
                ans+=1
        return ans 
            
        
        