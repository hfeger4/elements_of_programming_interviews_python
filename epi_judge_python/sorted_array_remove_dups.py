# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index -1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


def delete_duplicates_wrapper(A):
    idx = delete_duplicates(A)
    return A[:idx]


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('sorted_array_remove_dups.tsv',
                                              delete_duplicates_wrapper)
