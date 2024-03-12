class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        for start in range(len(arr)):
            total = 0
            for end in range(start, len(arr)):
                total += arr[end]
                if total == 0:
                    for i in range(start, end + 1):
                        arr[i] = 0
                    break
        
        alt = ListNode(0)
        a = alt
        for i in range(len(arr)):
            if arr[i] != 0:
                a.next = ListNode(arr[i])
                a = a.next
        a.next = None
        
        return alt.next
