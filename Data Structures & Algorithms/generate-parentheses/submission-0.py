class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def bt(inx, oc, cc, path, stack):
            print(path)
            if inx == n*2:
                result.append("".join(path))
                return

            if oc > 0:
                path.append("(")
                stack.append("(")
                bt(inx+1, oc-1, cc, path, stack)
                path.pop()
                stack.pop()
            
            if cc > 0:
               if len(stack)>0 and stack[-1]=="(":
                  le = stack.pop()
                  path.append(")")
                  bt(inx+1, oc, cc-1, path, stack)
                  stack.append(le)
                  path.pop()
        bt(0, n, n, [], [])
        return result







        