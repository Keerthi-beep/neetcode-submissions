class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in nums_set:
                cnt = 0
                x = nums[i]
                while x in nums_set:
                    cnt += 1
                    x += 1
                ans = max(cnt,ans)

        return ans