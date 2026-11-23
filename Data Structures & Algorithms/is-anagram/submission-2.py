class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # An Anagram is a word, phrase, or name formed by rearranging the letters of another
        ###__ How to solve __##
        # Check if both strings have all the same letters
        if sorted(s) == sorted(t):
            return True
        return False