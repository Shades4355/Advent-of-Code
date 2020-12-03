file = open("2020/03_data.txt", "r")

def slope(s_row:int, s_column:int, right:int, down:int, file):
  hill = []
  for line in file:
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
    
    if column >= len(hill[0])-1:
      column -= len(hill[0])-1
    
    position = hill[row][column]
    if position == "#":
      trees += 1
    
    print("row", str(row), "/", str(len(hill)-1))
    print("column", str(column), "/", str(len(hill[0])-1))
    print(position)
    print("trees:", str(trees))
    print("~" * 40)
    
  return trees


print(slope(0, 0, 3, 1, file))