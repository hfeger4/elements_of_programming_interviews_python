def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A



from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("int_as_array_increment.tsv",
                                              plus_one)
