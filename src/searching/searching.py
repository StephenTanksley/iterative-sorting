def linear_search(arr, target):
    # Your code here
    for item in arr:
        if item == target:
            return arr.index(item)
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    sorted = arr.sort()
    print(sorted)
    # Your code here

    return -1  # not found
