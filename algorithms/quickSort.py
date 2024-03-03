def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = len(arr) // 2
        left = [x for x in arr if x < arr[pivot]]
        right = [x for x in arr if x > arr[pivot]]
    
    return quickSort(left) + [arr[pivot]] + quickSort(right)