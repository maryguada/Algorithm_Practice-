# Write a function that takes in a non-empty array of distinct / unique integers representging a targer sum.
# The function should find all triplets in the array tha sum up to the target sum and return a two dimensional array of all these
# triplets. The numbers in each triplet shoul be ordered in ascending order, and the triplets themselves
# should be ordered in ascending order with respect to the numbers that they hold.

# If no three numbers sum up to the target sum, the function should return an empty array.

#-  START SOLUTION  -#
#--------------------#

# PSEUDOCODE:
# sort the array to find our triplets in O of 1 time.
# set a left pointer on index [1] call it left.
# set a pointer on the right index -1
# establish a current sum


def threeNumberSum(array, targetSum):
    # sorting takes n log n time
    array.sort()
    triplets = []

    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([arra[i], array[left], array[right]])
                left += 1
                right -= 1

    # incrementing left guarantees a greater current sum
            elif currentSum < targetSum:
                left += 1
    # decrementing right guarantees a less current sum
            elif currentSum > targetSum:
                right -= 1

    return triplets
