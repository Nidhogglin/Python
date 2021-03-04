#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 时间：2021/3/4 20:32

__author__ = 'Nidhogg'

"""
1. 两数之和
    给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 暴力枚举
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


# 哈希表
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashtable = dict()

        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num], i]
            hashtable[nums[i]] = i

        return []
