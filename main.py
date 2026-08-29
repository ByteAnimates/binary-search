"""Run it: python3 main.py"""

from binary_search import binary_search

NUMS = [4, 8, 15, 16, 23, 42, 108]


def main():
    for target in (16, 4, 108, 99):
        found = binary_search(NUMS, target)
        where = f"index {found}" if found != -1 else "not here"
        print(f"{target:>4}  →  {where}")


# Every value is findable at its own index, and nothing else is findable at all.
# Worth stepping through the second loop: it is the case people get wrong.
assert all(binary_search(NUMS, n) == i for i, n in enumerate(NUMS))
assert all(binary_search(NUMS, n) == -1 for n in (3, 9, 41, 109))
assert binary_search([], 1) == -1
assert binary_search([7], 7) == 0

if __name__ == '__main__':
    main()
