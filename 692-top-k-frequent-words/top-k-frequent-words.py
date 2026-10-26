class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        res = []
        freq = {}

        for word in words :
            freq[word] = freq.get(word , 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
        res = [p[0] for p in sorted_freq[:k]]
        return res