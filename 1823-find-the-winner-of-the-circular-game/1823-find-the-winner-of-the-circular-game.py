class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=0
        queue=deque([i for i in range(1,n+1)])
        while(len(queue)>1):
            c=k-1
            while c:
                queue.append(queue.popleft())
                c-=1
            queue.popleft()
        return queue[0]
            
            
            
            
            
            