def linear_search(arr, target):
    # Your code here
    iter = -1
    for i in arr:
        iter +=1
        if i == target:
            return iter

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
        left = 0
        right = len(arr) - 1

        while left <= right: 
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1  # not found
