# coding=utf-8

# Problem Description
# Easy Leetcode
# --------------------

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​
# customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the
# customer that has the maximum wealth.


# Solution
def maximum_wealth(accounts):
    """
    :param accounts: A 2D array of m x n integers
    :return: An integer
    """

    total_wealth = 0

    customer_ind = 0
    while customer_ind < len(accounts):

        wealth = 0

        bank_ind = 0
        while bank_ind < len(accounts[customer_ind]):

            wealth += accounts[customer_ind][bank_ind]

            bank_ind += 1
        customer_ind += 1

        if wealth > total_wealth:
            total_wealth = wealth

    print(total_wealth)


# m x n integer grid of accounts
account = [[1, 2, 3], [3, 2, 2]]

# Call to function
maximum_wealth(accounts=account)
