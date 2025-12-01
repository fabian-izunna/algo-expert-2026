class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_dict = {} #letter : frequency

        for letter in s:
            if letter in s_dict:
                freq = s_dict[letter]
                s_dict[letter] = freq + 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in s_dict:
                freq = s_dict[letter]
                if freq == 1:
                    del s_dict[letter]
                else:
                    s_dict[letter] = freq - 1
            else:
                return False

        return True
