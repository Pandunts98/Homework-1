x = int(input())
y = int(input())

moves = [[1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]]

for i, j in zip(*moves):
    print(x + i, y + j)
