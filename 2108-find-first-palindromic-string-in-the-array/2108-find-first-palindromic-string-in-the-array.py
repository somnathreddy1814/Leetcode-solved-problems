class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal_check(s):
            if s==s[::-1]:
                return True
            else:
                return False
        for word in words:
            if pal_check(word)==True:
                return word
                break
        return ""
        
                    