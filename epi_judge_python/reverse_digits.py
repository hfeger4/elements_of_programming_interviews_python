def reverse(x):
    result = 0
    remaining_x = abs(x)
    while remaining_x:
        result = result * 10 + remaining_x % 10
        remaining_x //= 10

    return -result if x < 0 else result


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('reverse_digits.tsv', reverse)
