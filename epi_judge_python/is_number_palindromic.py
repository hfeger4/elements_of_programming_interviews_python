def is_palindrome_number(x):
    # Implement this placeholder.
    x = str(x)
    return list(x)[::-1] == list(x)


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("is_number_palindromic.tsv",
                                              is_palindrome_number)
