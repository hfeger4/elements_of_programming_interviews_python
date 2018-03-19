import collections

from test_framework.test_failure_exception import TestFailureException
from test_framework.test_utils import enable_timer_hook


def even_odd(A):
    i = 0
    length = len(A) - 1
    while i < length:
        if A[i] % 2 == 0:
            i += 1
        else:
            A[i], A[length] = A[length], A[i]
            length -= 1





@enable_timer_hook
def even_odd_wrapper(timer, A):
    before = collections.Counter(A)

    timer.start()
    even_odd(A)
    timer.stop()

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailureException("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailureException("Elements mismatch")


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('even_odd_array.tsv',
                                              even_odd_wrapper)
