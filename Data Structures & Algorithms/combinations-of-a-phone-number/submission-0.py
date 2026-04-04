class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        m = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        def bt(path, inx):
            if inx == len(digits):
                result.append("".join(path[:]))
                return

            dic = m[int(digits[inx])]

            for l in dic:
                path.append(l)
                bt(path, inx+1)
                path.pop()
        if len(digits) == 0:
            return []
        bt([], 0)
        return result