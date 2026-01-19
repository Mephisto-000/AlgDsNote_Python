from typing import List, TypeVar

T = TypeVar("T")

def shell_sort(arr: List[T]) -> List[T]:
    if arr is None:
        raise TypeError("Input must be a list, not None")
    
    result = arr.copy()

    list_len = len(result)
    gap = list_len // 2
    while gap > 0:
        for n in range(gap, list_len):
            temp = result[n]
            m = n
            while m >= gap and result[m - gap] > temp:
                result[m] = result[m - gap]
                m = m - gap
            result[m] = temp
        gap = gap // 2

    return result
