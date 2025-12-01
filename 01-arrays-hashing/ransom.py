class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s_dict = {} #letter : frequency

        for letter in magazine:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in ransomNote:
            if letter in s_dict:
                if s_dict[letter] == 1:
                    del s_dict[letter]
                else:
                    s_dict[letter] -= 1
            else:
                return False

        return True
