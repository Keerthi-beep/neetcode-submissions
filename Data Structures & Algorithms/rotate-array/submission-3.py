class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        cnt = start = 0

        while cnt<n:
            curr = start
            prev = nums[start]
            while True:
                nxt = (curr+k)%n
                nums[nxt],prev = prev,nums[nxt]
                curr = nxt
                cnt += 1
                if start == curr:
                    break
            start += 1

                