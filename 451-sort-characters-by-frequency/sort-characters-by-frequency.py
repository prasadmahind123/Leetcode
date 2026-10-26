class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s :
            freq[ch] = freq.get(ch , 0) + 1

        sorted_freq = sorted(freq.items() , key = lambda item : (-item[1], item[0]))

        result = "".join(ch * count for ch, count in sorted_freq)

        return result
        