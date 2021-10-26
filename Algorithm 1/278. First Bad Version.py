# https://leetcode.com/problems/first-bad-version/
# Day 1
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i, j = 0, n
        
        while i < j:
            mid = (j-i)//2 + i
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        
        return i
        
