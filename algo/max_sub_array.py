import math


def find_max_crossing_subarray(arr, low, mid, high):
    max_left = 0
    max_right = 0
    left_sum = 0
    sum_a = 0
    i = mid
    while i >= low:
        sum_a += arr[i]
        if sum_a > left_sum:
            left_sum = sum_a
            max_left = i
        i -= 1
    right_sum = 0
    sum_b = 0
    j = mid + 1
    while j <= high:
        sum_b += arr[j]
        if sum_b > right_sum:
            right_sum = sum_b
            max_right = j
        j += 1
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = math.floor((low + high) // 2)
        left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_max_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_idx, high_idx, max_sum = find_max_subarray(a, 0, len(a) - 1)
print((low_idx, high_idx, max_sum))
print(f'Array range: [{a[low_idx]} - {a[high_idx]}] max-sum: {max_sum}')


# Code written by Kunal Gautam
