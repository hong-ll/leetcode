'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        g = []
        data = dict()
        for i in range(len(nums)):
            p = target - nums[i]
            if p in data:
                g.append(i)
                g.append(data[p])
                return g
            data[nums[i]] = i
        return g


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,5],9))