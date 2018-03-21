def apply_permutation(perm, A):
    for i in range(len(A)):
        next  = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("apply_permutation.tsv",
                                              apply_permutation_wrapper)
