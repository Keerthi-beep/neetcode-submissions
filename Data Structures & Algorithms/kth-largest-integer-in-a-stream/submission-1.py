class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.st = []
        self.nums = nums
        self.k = k
        # for i in range(len(nums)):
        #     if not self.st:
        #         self.st.append(nums[i])
        #         continue
        #     rev = []
        #     while self.st and self.st[-1]>nums[i]:
        #         rev.append(self.st.pop())
        #     self.st.append(nums[i])
        #     while rev:
        #         self.st.append(rev[-1])
        #         rev.pop()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]