class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ml = 0
        st = 0
        en = 0

        while en < len(s):
            if s[en] in m and st <= m[s[en]]:
                    st = m[s[en]] + 1
                    m[s[en]] = en
            else:
                m[s[en]] = en
                ml = max(ml, en-st+1)
            en += 1
        return ml
            


        