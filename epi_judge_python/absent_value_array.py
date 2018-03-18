from test_framework.test_failure_exception import TestFailureException


def find_missing_element(stream):
    # Implement this placeholder.
    return 0


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailureException('Unexpected no_missing_element exception')


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('absent_value_array.tsv',
                                              find_missing_element_wrapper)
