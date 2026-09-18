# Binary Search

**O(log n)** · [Watch the reel](https://www.facebook.com/reel/1062981399530986)

The working code from the [@ByteAnimates](https://www.facebook.com/ByteAnimates) reel.

```bash
python3 main.py
python3 binary_search.py
python3 test_binary_search.py
```

No dependencies. Python 3.9+.

### `binary_search.py`

```python
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
```

### Files

| | |
| --- | --- |
| `binary_search.py` | the reel snippet, generated from the episode |
| `main.py` | run this — the demo, with real inputs and real output |
| `test_binary_search.py` | the properties, checked — they survive a rewrite |

---

The snippet above is generated from the video itself — what you read is byte-for-byte
what was typed on screen. A fix to it belongs in the episode, so open an issue and the
next reel carries it. Everything else here is hand-written and welcome as a pull request.
