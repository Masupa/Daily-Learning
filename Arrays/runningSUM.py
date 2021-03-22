# coding=utf-8
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


# Easy Problem - Leetcode

def running_sum(arr):
    """
    :param arr: An array of integers
    :return: An array of integers which are the running sums
    """

    index = 1
    while index < len(arr):
        left_num = arr[index - 1]
        right_num = arr[index]

        arr[index] = left_num + right_num

        index += 1

    print(arr)


# Test Array
nums = [3,1,2,10,1]

# Call Functions
running_sum(arr=nums)
