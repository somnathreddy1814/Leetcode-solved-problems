class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str=""
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            new_str+=word1[i]
            i+=1
            new_str+=word2[j]
            j+=1
        if i<len(word1):
            new_str+=word1[i:]

        if j<len(word2):
            new_str+=word2[j:]
        return new_str