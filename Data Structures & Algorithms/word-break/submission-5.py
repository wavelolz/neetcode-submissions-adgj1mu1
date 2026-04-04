class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        arr = [False]*(len(s)+1)
        arr[len(s)]=True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    if arr[i]:
                        continue
                    arr[i] = arr[i+len(w)]
        print(arr)
        return arr[0]
        

        