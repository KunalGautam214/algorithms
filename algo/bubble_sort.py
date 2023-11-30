def bubble_sort(arr):
    length = len(arr)
    for _ in arr:
        i = length - 1
        while i > 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


# a = [5, 2, 4, 7, 1, 3, 2, 6, 0]
print("Enter space separated integer to sort an array\n")
a = list(map(int, list(input().split(' '))))
print('Original array', a)
bubble_sort(a)
print('Sorted array', a)


# Code written by Kunal Gautam
