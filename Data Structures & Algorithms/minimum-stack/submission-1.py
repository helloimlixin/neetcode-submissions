class MinStack:

    def __init__(self):
        self.stack = []
        self._min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self._min = val
        else:
            self.stack.append(val - self._min)
            self._min = min(self._min, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self._min = self._min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self._min
        else:
            return self._min

    def getMin(self) -> int:
        """One approach would to keep an additional stack of minimum values.
        """
        return self._min

        
