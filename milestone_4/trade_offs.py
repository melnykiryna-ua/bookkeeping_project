from typing import List, Tuple

# Option 1: time and space complexity is O(n^2)


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li) - 1):
            if li[i] + li[j] == target:
                return i, j
    return None


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}


# Option 2: time and space complexity is O(n)


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:

    seen = {}

    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
