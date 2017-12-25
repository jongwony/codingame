width = int(input())
height = int(input())
mat = [input() for _ in range(height)]


def get_idx(arr, i, j, direction=''):
    try:
        if arr[i][j] == '0':
            return j, i
        elif arr[i][j] == '.':
            if direction == 'down':
                return get_idx(arr, i + 1, j, 'down')
            elif direction == 'right':
                return get_idx(arr, i, j + 1, 'right')
    except IndexError:
        return -1, -1


def node_crawl(i, j):
    print(*get_idx(mat, i, j), *get_idx(mat, i, j + 1, 'right'), *get_idx(mat, i + 1, j, 'down'))


for i in range(height):
    for j in range(width):
        if mat[i][j] == '0':
            node_crawl(i, j)
