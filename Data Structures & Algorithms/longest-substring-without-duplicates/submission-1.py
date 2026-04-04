class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        st = 0
        en = 0
        record = []

        while en < len(s):
            if s[en] in record:
                while s[st] != s[en]:
                    record.remove(s[st])
                    st += 1
                st += 1
            else:
                record.append(s[en])
                n = en-st+1
                if n>ml:
                    ml = n
            en += 1
        return ml
            


        