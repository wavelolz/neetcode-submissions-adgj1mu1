from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = 0
        en = 0
        max_l = 0

        while en < len(s):
            counts = Counter(s[st:en+1])
            most_freq = counts.most_common()[0][1]
            if en-st+1 - most_freq <= k:
                max_l = max(max_l, en-st+1)
                en += 1
            else:
                while en-st+1 - most_freq > k:
                    st += 1
                    counts = Counter(s[st:en+1])
                    most_freq = counts.most_common()[0][1]
        return max_l 

        