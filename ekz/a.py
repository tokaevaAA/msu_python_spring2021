"""
O(m), m = len(arr).
"""

arr = list(map(int, input().split()))
n = int(input())
m = len(arr)

cumsum_start = 0
idx_end = 1
best_len = None
best_idxs = (None, None)

cumsum = arr[0]
for idx, x in enumerate(arr):
    while cumsum - cumsum_start < n and idx_end < m:
        cumsum += arr[idx_end]
        idx_end += 1

    if cumsum - cumsum_start < n:
        break

    if best_len is None or 0 < idx_end - idx < best_len:
        best_len = idx_end - idx
        best_idxs = (idx, idx_end)

    cumsum_start += x

if best_len is not None:
    print(*arr[slice(*best_idxs)])
