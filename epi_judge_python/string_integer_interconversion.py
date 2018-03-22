from test_framework.test_failure_exception import TestFailureException


def int_to_string(x):
        is_negative = False
        if x < 0:
            x, is_negative = -x, True

        x = []
        while True:
            s.append(chr(ord('0') + x % 10))
            x //= 10
            if x == 10:
                break
        return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-'], 0) * (-1 if s[0] == '-' else 1)
    )


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailureException("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailureException("String to int conversion failed")


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'string_integer_interconversion.tsv', wrapper)
