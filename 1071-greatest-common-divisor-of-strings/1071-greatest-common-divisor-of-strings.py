class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def greatest_common_divisor(n1,n2):
            while n2:
                n1,n2=n2,n1%n2
            return n1
        if str1+str2!=str2+str1:
            return ""
        elif str1==str2:
            return str1
        else:
            ln=greatest_common_divisor(len(str1),len(str2))
        return str1[:ln]
        
        
