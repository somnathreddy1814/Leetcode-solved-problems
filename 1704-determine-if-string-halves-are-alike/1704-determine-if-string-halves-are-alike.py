class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels='aeiouAEIOU'
        n=len(s)
        first_half=s[:n//2]
        second_half=s[n//2:]
        count_vowels_first=0
        count_vowels_second=0
        if len(first_half)==len(second_half):
            for i in range(n//2):
                if first_half[i] in vowels:
                    count_vowels_first+=1
            for j in range(n//2):
                if second_half[j] in vowels:
                    count_vowels_second+=1
        
        if count_vowels_first==count_vowels_second:
            return True
        else:
            return False
            
            
        