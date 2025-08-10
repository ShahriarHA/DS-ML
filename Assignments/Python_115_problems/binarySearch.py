def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the number to search: "))
result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in the list")
