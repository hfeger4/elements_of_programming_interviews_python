def find_anagrams(dictionary):
    # Implement this placeholder.
    return []


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        "anagrams.tsv", find_anagrams, comp=test_utils.unordered_compare)
