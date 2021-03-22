# Problem Description
# Easy Leetcode
# --------------------

# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example
# --------------------
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


# Solution
# --------------------
def num_identical_pairs(nums):
    """
    :param nums: An array of integers
    :return:
    """

    number_good_pairs = 0

    pointer_one = 0
    while pointer_one < len(nums):

        pointer_two = pointer_one + 1
        while pointer_two < len(nums):
            if (nums[pointer_one] == nums[pointer_two]) and (pointer_one < pointer_two):
                number_good_pairs += 1
            pointer_two += 1
        pointer_one += 1

    print(number_good_pairs)


def num_identical_pairs_two(nums):
    """
    :param nums: An array of integers
    :return:
    """

    nums.sort() # Sort list

    count = 0

    pointer_one = 0
    while pointer_one < len(nums):
        pointer_two = pointer_one + 1
        while pointer_two < len(nums):
            if (nums[pointer_one] == nums[pointer_two]) and (pointer_one < pointer_two):
                count += 1
            elif nums[pointer_one] < nums[pointer_two]:
                pointer_two = len(nums)

            pointer_two += 1
        pointer_one += 1

    print(count)


# Input
sample_input = [1, 2, 3, 1, 1, 3]

# Call to function
num_identical_pairs_two(nums=sample_input)
