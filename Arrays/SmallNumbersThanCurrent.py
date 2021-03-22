# Problem Description
# Easy Leetcode
# -------------------

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for
# each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Example
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]


# Solution
def small_numbers_than_current(nums):
    """
    :param nums: An array of integers
    :return: An array of integers
    """

    return_list = list()

    pointer_one = 0
    while pointer_one < len(nums):

        count = 0

        pointer_two = 0
        while pointer_two < len(nums):
            if (pointer_one != pointer_two) and (nums[pointer_one] > nums[pointer_two]):
                count += 1

            pointer_two += 1

        return_list.append(count)
        pointer_one += 1

    print(return_list)


# Sample Input
sample_input = [8, 1, 2, 2, 3]

# Call to function
small_numbers_than_current(nums=sample_input)