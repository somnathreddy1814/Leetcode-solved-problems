class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dct=Counter(nums)
        arr=list(dct.keys())
        if len(nums)==1:
            return 1
        freqs=list(dct.values())
        
        mx=max(freqs)
        if mx==1:
            return len(arr)
        print(freqs)
        final=0
        for i in range(len(freqs)):
            if freqs[i]==mx:
                final+=mx
        return final

        
        