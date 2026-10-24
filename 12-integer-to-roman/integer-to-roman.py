class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L" , "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ans = ''
        i = 0
        while num > 0 :
            if value[i] > num :
                 i += 1
            else :
                ans += symbol[i]
                num -= value[i]
            
        
        return ans
