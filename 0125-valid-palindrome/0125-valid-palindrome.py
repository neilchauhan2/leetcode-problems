class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if self.isAlphanumeric(s[left].lower()) and self.isAlphanumeric(s[right].lower()):
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left, right = left + 1, right - 1
            else:
                while left < len(s) and not self.isAlphanumeric(s[left].lower()):
                    left+= 1
                
                while right >= 0 and not self.isAlphanumeric(s[right].lower()):
                    right-=1
        
        return True


    def isAlphanumeric(self, s):
        return (
            (ord('A') <= ord(s) <= ord('Z')) or
            (ord('a') <= ord(s) <= ord('z')) or
            (ord('0') <= ord(s) <= ord('9'))
        )




