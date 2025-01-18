w,h = map(int, input("Please enter the amount of players and the amount of splits. (nP nS)").split())
connections = [[0 for i in range(w-1)] for j in range(h)]
turns = int(input("Please enter the turns of the players. (nT)"))
# prize_enable = input("Would you like to enable prizes? (Y/N)") == "Y" or False
DBG = False
prizes = [""] * w
def print_table(debug=False):
    print("        ", end="")
    for i in range(w):
        print(f"P{i+1}", end=f"{' '*(len(str((w-1)*h))+2)}")
    print()
    c = 0
    for i in range(h):
        print(f"Split{str(i+1).zfill(len(str(h)))} ", end="")
        for j in range(w-1):
            c+=1
            print("|", end=" ")
            print(f" {"-"*len(str((w-1)*h))}" if connections[i][j] == 1 else f" {str(c).zfill(len(str((w-1)*h)))}", end=" ")
            
        print("|",connections[i] if debug else "")
    # if prize_enable:
    #     print("Prizes: ", prizes)
print_table(DBG)
turn = 1
while True:
    
    turn %= w 
    if turn == 0:
        turns -= 1
        turn = 1
    print(f"Player {turn} please enter the number of the split. (NumberOfSplit)\n You have {turns} turns left. Should you exit, please enter '-999'.")
    try:
        # nos = 0
        # pos, split = map(int, input().split())# Y,X
        nos = int(input()) - 1
        split = nos // (w-1) + 1
        pos = nos % (w-1) + 1
        # split = nos // w
        # pos = nos % w + 1
        print(f"X: {pos}, Y: {split}")
    except ValueError:
        print("Invalid input.")
        continue
    if split > h or pos > w-1:
        print("Invalid split or position.")
        continue

    if nos == -999 or (split == 0 and pos == 0):
        break
    #check if the connection already exists, check left and right, if xpos is 0, check right, if xpos is w-1ONLY, check left ONLY
    if pos != 0 and pos != w-1:
        if connections[split-1][pos-2] == 1 or connections[split-1][pos] == 1:
            print("Connection illegal.")
            continue
    if pos == w-1:
        if connections[split-1][pos-2] == 1:
            print("Connection illegal.")
            continue
    if pos == 1:
        if connections[split-1][pos] == 1:
            print("Connection illegal.")
            continue
    if connections[split-1][pos-1] == 1:
        print("Connection exists.")
        continue
    turn +=1
    connections[split-1][pos-1] = 1
    print_table(DBG)

    if turns == 0:
        break
print_table(DBG)
def traverse_ghost_leg(grid, start):
    position = start
    for rung in grid:
        if position > 0 and rung[position - 1] == 1:
            position -= 1
        elif position < len(rung) - 1 and rung[position] == 1:
            position += 1
    return position
connections.append([0 for i in range(w-1)])
for i in range(w):
    grid = connections
    start_position = i
    end_position = traverse_ghost_leg(grid, start_position)
    print(f"Start at line {start_position+1}, end at line {end_position+1}")

# dfslist = [[0 for i in range(w-1+w)] for j in range(h)]
# for i,j in enumerate(dfslist):
#     for k,l in enumerate(j):
#         if k % 2 == 0:
#             dfslist[i][k] = 1
#         else:
#             dfslist[i][k] = connections[i][k//2]
# print(*dfslist,sep="\n")
# def find_path(dfslist, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     for i in range(len(dfslist[start])):
#         if dfslist[start][i] == 1 and i//2 not in path:
#             newpath = find_path(dfslist, i//2, end, path)
#             if newpath:
#                 return newpath
#     return None
# def find_all_paths(dfslist):
#     paths = []
#     for i in range(h):
#         for j in range(h):
#             if i != j:
#                 path = find_path(dfslist, i, j)
#                 if path:
#                     paths.append(path)
#     return paths
# paths = find_all_paths(dfslist)
# print(*paths,sep="\n")




