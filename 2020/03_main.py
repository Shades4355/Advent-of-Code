
def slope(s_row:int, s_column:int, right:int, down:int):
  file = open("2020/03_data.txt", "r")
  hill = []
  for line in file:
    line = line.strip("\n")
    row = []
    for character in line:
      row.append(character)
    hill.append(row)

  row = s_row
  column = s_column
  trees = 0
  while row < len(hill) - 1:
    row += down
    column += right
    
    if column >= len(hill[0]):
      column -= len(hill[0])
    
    position = hill[row][column]
    if position == "#":
      trees += 1
  file.close()
  return trees

# part 1 #
print("Part 1:", slope(0, 0, 3, 1)) # 145


# part 2 #
slope1 = slope(0, 0, 1, 1) 
slope2 = slope(0, 0, 3, 1)
slope3 = slope(0, 0, 5, 1)
slope4 = slope(0, 0, 7, 1)
slope5 = slope(0, 0, 1, 2)

total_trees = slope1 * slope2 * slope3 * slope4 * slope5
print("Part 2:", total_trees) # 3424528800