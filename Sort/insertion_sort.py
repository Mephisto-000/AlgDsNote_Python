from typing import List, TypeVar

T = TypeVar("T")

def insertion_sort(arr: List[T]) -> List[T]:
    if arr is None:
        raise TypeError("Input must be a list, not None")
    
    result = arr.copy()

    list_len = len(result)
    for n in range(list_len-1):
        key = result[n + 1]
        m = n
        while m >= 0 and key < result[m]:
            result[m+1] = result[m]
            m -= 1
        result[m+1] = key
    
    return result
