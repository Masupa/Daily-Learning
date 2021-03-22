
# Problem Description

# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith
# kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
# greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

# Example

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]


# Easy Problem


def kids_with_candies(candies, extra_candies):
    """
    :param candies: An array of representing the number of candies each kid has
    :param extra_candies: An int representing extra candies
    :return: An array of boolean values representing whether a kid would have the greatest number of candies
    """

    # Return list
    return_list = list()

    # Find maximum value # Run in O(n)
    max_candies = max(candies)

    index = 0
    while index < len(candies):
        if (candies[index] + extra_candies) >= max_candies:
            return_list.append(True)
        else:
            return_list.append(False)

        index += 1

    print(return_list)


# Number of candies per kid
candies = [2, 3, 5, 1, 3]

# Extra Candies
extra_candies = 3

kids_with_candies(candies, extra_candies)
