def insertion_sort(a, length):
    for i in range(length):
        key = a[i]
        j = i - 1

        # shift array element to right if left element > right element
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        # place lower array element at correct position when while loop breaks
        a[j + 1] = key


# a = [5, 2, 4, 7, 1, 3, 2, 6]
print("Enter space separated integer to sort an array\n")
a = list(map(int, list(input().split(' '))))
print('Original array', a)
insertion_sort(a, len(a))
print('Sorted array', a)


# Code written by Kunal Gautam
