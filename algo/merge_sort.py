def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # create Left and Right array with n1 and n2 size respectively
    L = [0] * (n1)
    R = [0] * (n2)

    # get all left array elements in Left array
    for i in range(n1):
        # L[i] = (a[p + i - 1])
        L[i] = (a[p + i])

    # get all right array elements in Left array
    for j in range(n2):
        # R[j] = (a[q + j])
        R[j] = (a[q + j + 1])
    i = 0
    j = 0
    k = p
    # for k in range(r):
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # if i < n1 then assign all remaining elements to array
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # if j < n2 then assign all remaining elements to array
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


# a = [5, 2, 4, 7, 1, 3, 2, 6]
print("Enter space separated integer to sort an array\n")
a = list(map(int, list(input().split(' '))))
print('Original array', a)
merge_sort(a, 0, len(a) - 1)
print('Sorted array', a)


# Code written by Kunal Gautam
