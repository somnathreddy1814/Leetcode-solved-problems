class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
       
        ans=[]
        for key,val in sorted(count.items(),key=lambda x:(-x[1],x[0])):
            ans+=[key]*val
        return "".join(ans)
    
    
    
    
# def frequencySort(self, s: str) -> str:
# 	# Count the occurence on each character
# 	cnt = collections.defaultdict(int)
# 	for c in s:
# 		cnt[c] += 1
	
# 	# Sort and Build string
# 	res = []
# 	for k, v in sorted(cnt.items(), key = lambda x: -x[1]):
# 		res += [k] * v
# 	return "".join(res)


# class Solution:
#     def frequencySort(self, s: str) -> str:     #   Example:   s = "bAaCbb"

#         ctr = Counter(s)                        #       ctr = {'b':3, 'A':1, 'a':1, 'C':1}

#         d   = list(ctr.items())                 #         d = [('b',3), ('C',1), ('a',1), ('A',1)]

#         d.sort(key = lambda x: (-x[1], x[0]))   #         d = [('b',3), ('A',1), ('C',1), ('a',1)]

#         words = [ch*n for ch, n in d]           #     words = ['bbb', 'A', 'C', 'a']

#         ans = ''.join(words)                    #       ans = 'bbbACa'

#         return ans
