# Binary Search — O(log n)
# As shown in the reel: https://www.facebook.com/reel/1062981399530986
# Generated from the episode; edits here are overwritten. See the README.

def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
