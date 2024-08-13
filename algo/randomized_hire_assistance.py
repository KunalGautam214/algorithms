def hire_assistance(candidate_list):
    best = 0
    # iterate all the candidate
    for i in candidate_list:
        # if candidate is better than best then change the best candidate
        if i > best:
            best = i
    return best


a_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a_3 = [5, 2, 1, 8, 4, 7, 10, 9, 3, 6]

hired_candidate = hire_assistance(a_3)
print(hired_candidate)
