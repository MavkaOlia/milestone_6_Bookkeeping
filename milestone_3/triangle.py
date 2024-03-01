import sys


def print_pascals_triangle(rows: int):
    if rows <= 0:
        print("Number of rows must be greater than 0.")
        return

    triangle = [[1] * (i + 1) for i in range(rows)]

    for i in range(2, rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    width = len(str(triangle[-1][-1]))

    for row in triangle:
        print(' '.join(f'{num:>{width}}' for num in row).center(width * len(row)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python triangle.py <rows>")
        sys.exit(1)

    try:
        rows = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide a valid number of rows.")
        sys.exit(1)

    print_pascals_triangle(rows)


    from typing import List

def find_max(li: List[int]) -> int:
    max_val = li[0]
    for num in li:
        max_val = max_val if max_val >= num else num

    return max_val
        
print(find_max([5, 7, 3, 8]))
print('O(n)')