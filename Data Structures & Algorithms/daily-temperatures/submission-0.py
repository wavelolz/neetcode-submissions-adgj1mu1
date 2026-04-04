class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        r = []

        for i in range(len(temperatures)):
            stack.append([temperatures[i], i, 0])

            for j in range(len(stack)-2, -1, -1):
                stack[j][2] += 1
            
            cur_val = stack[-1][0]
            for k in range(len(stack)-2, -1, -1):
                if cur_val > stack[k][0]:
                    rm = stack.pop(k)
                    r.append(rm)
        while len(stack)>0:
            rm = stack.pop()
            rm[2] = 0
            r.append(rm)

        r = sorted(r, key=lambda x: x[1])
        res = [i[2] for i in r]
        return res


        