
#map is a 10*10 matrix and each element is a dictionary
#"height">height of each box
#"colous"> 0:grey, 1:blue, -1: yellow
##so that current map is 10*10 flat plane with all blue squares
map = [[{} for _ in range(10)] for _ in range(10)]##lists are starting from top left corner of the matrix
colour_stat = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
height_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(10):
  for j in range(10):
    map[i][j] = {"height": height_list[i*10+j], "colour": colour_stat[i*10+j]}

  def lightboat(array):#start at 0,0(top left corner facing right)
  print("WELCOME!")
  print("staring point: top left corner facing right")
  ymax = len(map)
  xmax = len(map[0])
  x=0 ##j in for loop
  y=0 ##i in for loop
  direction = 0 ## 0-east 1-south 2-west 3-north so that i can increase the direction by 1 for every clockwise turn
  commands = input("enter commands(use spaces inbetween):")
  commands_list = commands.split()
  for k in range(len(commands_list)):
    if commands_list[k]=="^":
      if direction == 0:
        if map[y][x]["height"] == map[y][x+1]["height"]:
          x = x+1
      if direction == 1:
        if map[y][x]["height"] == map[y+1][x]["height"]:
          y = y+1
      if direction == 2:
        if map[y][x]["height"] == map[y][x-1]["height"]:
          x = x-1
      if direction == 3:
        if map[y][x]["height"] == map[y-1][x]["height"]:
          y = y-1
    if commands_list[k]=="*":
      if direction == 0:
        if abs(map[y][x]["height"] - map[y][x+1]["height"])==1:
          x = x+1
      if direction == 1:
        if abs(map[y][x]["height"] - map[y+1][x]["height"])==1:
          y = y+1
      if direction == 2:
        if abs(map[y][x]["height"] - map[y][x-1]["height"])==1:
          x = x-1
      if direction == 3:
        if abs(map[y][x]["height"] - map[y-1][x]["height"])==1:
          y = y-1
    if commands_list[k]=="<":
      direction = (direction-1)%4
    if commands_list[k]==">":
      direction = (direction+1)%4
    if commands_list[k]=="@":
      map[y][x]["colour"] = -1*map[y][x]["colour"]
    if (x == xmax) or (y == ymax):
      print("hehe you fell off")
      break

  print("x:", x, "
 y:", y, "
 direction:", direction)
  final_map = [[0 for _ in range(xmax)] for _ in range(ymax)]
  for i in range(ymax):
    for j in range(xmax):
      final_map[i][j] = map[i][j]["colour"]
  for i in range(ymax):
    print(final_map[i])
  return "Succesfully completed"
  