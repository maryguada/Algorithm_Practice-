# In ascending order from left to right, small to high
# has to be done in place

# O(n^2 time) | O(1) space


def bubbleSort(arr):
    isSorted = False  # set an is Sorted variable
    counter = 0

    while not isSorted:

        isSorted = True
        # this only takes in until the second to last item in arr
        # bc you need to compare the second to last and the last item in arr

        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i+1]:
                swap(i, i+1, arr)
                isSorted = False  # our array is not Sorted.
        counter += 1
    return arr

# helper swap function :


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


a_arr = [8, 7, 3, 2, 11]
b_arr = [9, 3, 5, 100, 888]
print(bubbleSort(a_arr))
print(bubbleSort(b_arr))
