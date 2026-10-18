class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = ""
        for ch in s :
            if ch.isalnum() :
                strs += ch

        reverse = strs[ :: -1]
        if reverse == strs:
            return True

        return False
        