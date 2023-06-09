def main():
    arr = [
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 1],
    ]

    print("Before:")
    for row in arr:
        print(row)

    convert_neighbour(arr, 3, 1)

    print("After:")
    for row in arr:
        print(row)


def convert_neighbour(arr, i, j):
    n = len(arr)
    if n == 0:
        return arr

    m = len(arr[0])
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[False for _ in range(m)] for _ in range(n)]

    dfs(arr, i, j, visited, moves, n, m)

    return arr


def dfs(arr, i, j, visited, moves, n, m):
    # implement this function


def in_range(n, m, i, j):
    return 0 <= i < n and 0 <= j < m


if __name__ == "__main__":
    main()
