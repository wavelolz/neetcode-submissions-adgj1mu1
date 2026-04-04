class Solution:
    def numDecodings(self, s: str) -> int:
        m = {chr(key): 0 for key in range(ord("A"), ord("Z")+1)}
        cnt = 1
        for key in m:
            m[key] = str(cnt)
            cnt += 1

        if len(s) == 0:
            return 0
        arr = [0]*len(s)
        if s[0] == "0":
            arr[0] = 0
        else:
            arr[0] = 1
        
        if len(s) == 1:
            return arr[0]

        if s[1] in m.values() and s[:2] in m.values():
            arr[1] = arr[0]+1
        elif s[1] in m.values():
            arr[1] = arr[0]
        elif s[:2] in m.values():
            arr[1] = arr[0]
        else:
            return 0  


        for i in range(2, len(s)):
            if s[i] in m.values() and s[i-1:i+1] in m.values():
                arr[i] = arr[i-2] + arr[i-1]
            elif s[i] in m.values():
                arr[i] = arr[i-1]
            elif s[i-1:i+1] in m.values():
                arr[i] = arr[i-2]
            else:
                return 0
        print(arr)
        return arr[len(s)-1]

        



        