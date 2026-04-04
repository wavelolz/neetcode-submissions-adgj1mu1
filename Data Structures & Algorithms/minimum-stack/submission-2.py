import numpy as np
class MinStack:

    def __init__(self):
        self.stack = []
        self.minValL = []
        self.minVal = float("inf")
        

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        
        self.minValL.append(self.minVal)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minValL.pop()
        if len(self.minValL)>0:
            self.minVal = self.minValL[-1]
        else:
            self.minVal = float("inf")
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
        
