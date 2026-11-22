class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0


        for i in range(len(s)) :
            for j in range(len(s)) :
                new_s = s[i : j + 1]
                new_s = new_s.strip()

                if new_s == "" :
                    continue

                reversed_s = new_s[ :: -1]
                
                if new_s == reversed_s :
                    count += 1 

        return count
        