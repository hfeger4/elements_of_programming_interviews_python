from test_framework.test_utils import enable_timer_hook


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume


def calculate_traffic_volumes(A, w):
    # Implement this placeholder.
    return []


@enable_timer_hook
def calculate_traffic_volumes_wrapper(timer, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    timer.start()
    result = calculate_traffic_volumes(A, w)
    timer.stop()

    return [(x.time, x.volume) for x in result]


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'max_of_sliding_window.tsv', calculate_traffic_volumes_wrapper)
