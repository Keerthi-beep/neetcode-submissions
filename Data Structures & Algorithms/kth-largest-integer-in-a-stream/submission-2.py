class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.st = []
        self.nums = nums
        self.k = k
        
        for i in range(len(self.nums)):
            self.add_val(self.nums[i])
        #self.nums = self.st

    def add_val(self, val: int) -> int:
        if not self.st:
            self.st.append(val)
            return
        rev = []
        while self.st and self.st[-1]>val:
            rev.append(self.st.pop())
            print(rev)
        self.st.append(val)
        while rev:
            self.st.append(rev[-1])
            rev.pop()

    def add(self, val: int) -> int:
        self.add_val(val)
        return self.st[-self.k]