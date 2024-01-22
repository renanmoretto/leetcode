# def solution(board: list[list[str]]) -> bool:
#     N_ROWS = 9
#     N_COLS = 9

#     # Create rows and cols ints
#     rows = []
#     for row in board:
#         nums = [int(n) if n != '.' else float('nan') for n in row]
#         rows.append(nums)

#     cols = []
#     for n_col in range(N_COLS):
#         col = [int(row[n_col]) if row[n_col] != '.' else float('nan') for row in board]
#         cols.append(col)

#     # Verify rows
#     for row in rows:
#         if len(set(row)) != len(row):
#             return False

#     # Verify cols
#     for col in cols:
#         if len(set(col)) != len(col):
#             return False

#     # Verify box
#     boxes_coord = []
#     for i in range(len(rows) // 3):
#         for j in range(len(rows) // 3):
#             boxes_coord.append((i, j))

#     boxes = [[[], [], []], [[], [], []], [[], [], []]]
#     for i_row, row in enumerate(rows):
#         box_i_chunk = i_row // 3
#         for i_num_row in range(len(row)):
#             i_box = i_num_row // 3
#             boxes[box_i_chunk][i_box].append(row[i_num_row])

#     for box_group in boxes:
#         for box in box_group:
#             if len(set(box)) != len(box):
#                 return False

#     # boxes = [[], [], [], [], [], [], [], [], []]
#     # for i_row, row in enumerate(rows):
#     #     for i_num_row in range(len(row)):
#     #         box_num = (i_row // 3, i_num_row // 3)
#     #         print(i_row, i_num_row, box_num)
#     #         # boxes[i_box].append(row[i_num_row])

#     return True


def solution(board: list[list[str]]) -> bool:
    BOARD_SIZE = 9

    rows = [[] for _ in range(BOARD_SIZE)]
    cols = [[] for _ in range(BOARD_SIZE)]
    boxes = [[] for _ in range(BOARD_SIZE)]

    for i in range(len(board)):
        for j in range(len(board)):
            value = board[i][j]

            if value == '.':
                continue

            if value in rows[i] or value in cols[j]:
                return False

            rows[i].append(value)
            cols[j].append(value)
            box_index = (i // 3) * 3 + (j // 3)
            boxes[box_index].append(value)

    for box in boxes:
        if len(set(box)) != len(box):
            return False

    return True


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]

    r = solution(board)
    print(r)
