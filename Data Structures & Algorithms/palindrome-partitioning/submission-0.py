class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        def isPalin(s):
            left_inx = 0
            right_inx = len(s)-1

            while left_inx <= right_inx:
                if s[left_inx] != s[right_inx]:
                    return False
                left_inx += 1
                right_inx -= 1
            return True

        def bt(left_inx, right_inx, path):

            if right_inx == len(s):
                result.append(path[:])
                return

            for i in range(right_inx, len(s)):
                if isPalin(s[left_inx:i+1]):
                    path.append(s[left_inx:i+1])
                    bt(i+1, i+1, path)
                    path.pop()
        bt(0, 0, [])
        return result



        