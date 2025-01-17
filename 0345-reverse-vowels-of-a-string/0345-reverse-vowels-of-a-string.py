class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        i = 0
        j = len(s) - 1
        s = list(s)

        while i <= j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                (s[i], s[j]) = (s[j], s[i])
                i+=1
                j-=1
            else:
                if s[i].lower() not in vowels:
                    i+=1

                if s[j].lower() not in vowels:
                    j-=1

        return "".join(s) 
