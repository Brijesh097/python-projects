row_1 = ["X", "X", "X"]
row_2 = ["X", "X", "X"]
row_3 = ["X", "X", "X"]

map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

position = input("Where do you want to put the treasure?\n")

row = int(position[0])
col = int(position[1])

map[row - 1][col - 1] = "💰"

print(f"{row_1}\n{row_2}\n{row_3}")
