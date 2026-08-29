"""
Run it: python3 test_binary_search.py   (or: pytest)
"""

from binary_search import binary_search
from main import NUMS


def test_every_value_is_found_at_its_own_index():
    assert all(binary_search(NUMS, n) == i for i, n in enumerate(NUMS))


def test_missing_values_report_minus_one():
    # The case people get wrong: the loop has to END, and end with -1, rather than
    # narrowing forever or falling off an edge.
    for n in (3, 9, 41, 109):
        assert binary_search(NUMS, n) == -1


def test_it_agrees_with_a_linear_scan_on_every_value_in_range():
    for target in range(0, 120):
        want = NUMS.index(target) if target in NUMS else -1
        assert binary_search(NUMS, target) == want, target


def test_edge_cases():
    assert binary_search([], 1) == -1
    assert binary_search([7], 7) == 0
    assert binary_search([7], 8) == -1
    assert binary_search([1, 2], 2) == 1


def test_it_really_is_logarithmic():
    # Halving means a thousand values cost ten looks, not a thousand. Counted rather
    # than asserted: the loop below mirrors the snippet exactly.
    import math

    def looks(n, target):
        a = list(range(n))
        lo, hi, seen = 0, len(a) - 1, 0
        while lo <= hi:
            seen += 1
            mid = (lo + hi) // 2
            if a[mid] == target:
                return seen
            if a[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return seen

    for n in (10, 100, 1000, 10000):
        assert looks(n, n - 1) <= math.ceil(math.log2(n + 1))


if __name__ == '__main__':
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
            passed += 1
    print(f'\n{passed} tests passed\n')
