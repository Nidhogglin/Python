#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 时间：2021/3/4 21:42

__author__ = 'Nidhogg'

"""
26. 删除排序数组中的重复项
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 我的解法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        i = 1

        while i < n:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                n -= 1
                i -= 1
            i += 1

        return n


# 快慢指针
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1



