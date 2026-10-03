class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        r1, r2 = set(), set()
        for i in range(len(nums1)):
            if nums1[i] not in n2:
                r1.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] not in n1:
                r2.add(nums2[i])

        return [list(r1),list(r2)]