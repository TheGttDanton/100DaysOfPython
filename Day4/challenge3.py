row1 = ["😜", "😜", "😜"]
row2 = ["😜", "😜", "😜"]
row3 = ["😜", "😜", "😜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

location = int(input("Where you want to hide the treasure? \n"))
column = int(location / 10) - 1
row = int(location % 10) - 1

map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")
