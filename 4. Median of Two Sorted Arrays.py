# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        res = l//2
        if l%2==0:
            return (nums1[res] + nums1[res-1])/2
        else:
            return nums1[res]
