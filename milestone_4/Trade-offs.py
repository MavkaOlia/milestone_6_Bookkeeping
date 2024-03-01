from typing import List, Tuple


# Approach 1, using nested for loop
def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return i, j


print("Time complexity is: O(n^2)")
print("space complexity is O(1)")
assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

# Approach 2, using set

def find_sum_2(target: int, li: List[int]) -> Tuple[int, int]:
    set_list = set()

    for x in li:
        complement = target - x

        if complement in set_list:
            return complement, x

        set_list.add(x)


print("Time complexity is: O(n)")
print("space complexity is O(n)")
assert find_sum_2(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

