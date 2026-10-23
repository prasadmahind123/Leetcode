class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")

        if len(s) != len(pattern) :
            return False

        map_p = {}
        map_s = {}

        for i in range(len(pattern)) :
            if pattern[i] not in map_p :
                map_p[pattern[i]] = s[i]
            elif map_p[pattern[i]] != s[i] :
                return False

            if s[i] not in map_s :
                map_s[s[i]] = pattern[i]
            elif map_s[s[i]] != pattern[i] :
                return False

        return True
        