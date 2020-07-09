def linear_search(arr, target):
    # Your code here
    for item in arr:
        if item == target:
            return arr.index(item)
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = (len(arr) - 1)

    while start <= end:
        mid = (start + end) // 2
        check = arr[mid]

        if check == target:
            return arr.index(check)
        if check > target:
            end = mid - 1
        elif check < target:
            start = mid + 1

    return -1
