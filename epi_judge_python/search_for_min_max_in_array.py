import collections

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    # Implement this placeholder.
    return MinMax(0, 0)


def res_printer(expected, result):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    return fmt(expected), fmt(result)


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'search_for_min_max_in_array.tsv',
        find_min_max,
        res_printer=res_printer)
