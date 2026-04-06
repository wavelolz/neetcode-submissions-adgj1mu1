class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # extract the frequency array of s1, if s2 contains substring with
        # the same frequency array then we found it
        m = {}
        for i in range(len(s1)):
            m[s1[i]] = 1 + m.get(s1[i], 0)

        tmp_m = m.copy()
        st = 0
        for en in range(len(s2)):
            if s2[en] in tmp_m and tmp_m[s2[en]] > 0:
                tmp_m[s2[en]] -= 1
                if en-st+1 == len(s1):
                    return True
            elif s2[en] not in tmp_m:
                st = en + 1
                tmp_m = m.copy()
            elif tmp_m[s2[en]] == 0:
                while s2[st] != s2[en]:
                    tmp_m[s2[st]] += 1
                    st += 1
                st += 1
        return False

