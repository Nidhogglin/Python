#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/22 12:26

class Solution:

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        if len(nums) == 1:
            a.append(nums)
            return a
        for i in nums:
            a.append([i, self.permute(nums.pop(i))])
        return a


s = Solution
a = [1,2,3]
print(s.permute(a))