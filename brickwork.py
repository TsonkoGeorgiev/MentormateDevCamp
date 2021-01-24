from collections import deque


def build_two_brick_rows(m, layer_input):
    new_layer = [[0 for _ in range(m)]for _ in range(2)]

    for i in range(2):
        for col in range(m - 1):
            if i == 0:
                if new_layer[i][col] == 0:
                    if layer_input[i][col] == layer_input[i][col + 1]:
                        brick = bricks.popleft()
                        new_layer[i][col] = brick
                        new_layer[i + 1][col] = brick
                    else:
                        brick = bricks.popleft()
                        new_layer[i][col] = brick
                        new_layer[i][col + 1] = brick
            else:
                if new_layer[i][col] == 0:
                    brick = bricks.popleft()
                    new_layer[i][col] = brick
                    new_layer[i][col + 1] = brick

    return new_layer


def validate_n_m(wall):
    n = len(wall)
    m = len(wall[0])
    if n <= 100 and m <= 100:
        return 'Area is valid with less than 100 lines/columns'
    return 'Invalid area'


def validate_no_brick_lies_on_three_rows_cols(inventory):
    for value in inventory.values():
        if value > 2:
            return 'A brick lies on 3 rows/cols'
    return 'No brick lies on 3 rows/cols'


layer_one = []
rows, cols = [int(x) for x in input().split()]
for _ in range(rows):
    line = [int(x) for x in input().split()]
    layer_one.append(line)


bricks_count = (rows * cols) / 2
bricks = deque([x + 1 for x in range(int(bricks_count))])

layer_two = deque()
layer = deque()

for _ in range(int(rows/2)):
    for _ in range(2):
        layer.appendleft(layer_one.pop())
    layer_rebuilt = build_two_brick_rows(cols, layer)
    for _ in range(2):
        layer_two.appendleft(layer_rebuilt.pop())
    layer.clear()


output = ''
for row in layer_two:
    output += f"{' '.join([str(item) for item in row])}\n"

bricks_dict = {}
for row in layer_two:
    for item in row:
        if str(item) not in bricks_dict:
            bricks_dict[str(item)] = 0
        bricks_dict[str(item)] += 1


print(output)

print(validate_n_m(layer_two))

print(validate_no_brick_lies_on_three_rows_cols(bricks_dict))







