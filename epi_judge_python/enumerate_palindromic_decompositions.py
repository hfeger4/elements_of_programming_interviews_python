def palindrome_decompositions(input):
    # Implement this placeholder.
    return []


def comp(a, b):
    return sorted(a) == sorted(b)


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'enumerate_palindromic_decompositions.tsv', palindrome_decompositions,
        comp)
