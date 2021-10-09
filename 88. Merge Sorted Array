#https://leetcode.com/problems/merge-sorted-array/submissions/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums2[:n]
        while len(nums1)!=m:
            del nums1[-1]
        nums1.extend(temp)
        nums1.sort()
