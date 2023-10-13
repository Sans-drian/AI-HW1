import queue

#setting up the maze
def createMaze():
    maze = []
    maze.append(["#", "S", "#", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "G", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"])

    return maze

# function to print the maze
def printMaze (maze, path = ""):
    for x, pos in enumerate(maze[0]):
        if pos == "S":
            start = x
    
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end = "")
            else:
                print(col + " ", end = "")
        print()

# function to validate the moves
def valid(maze, moves):
    start = None
    for x, pos in enumerate(maze[0]):
        if pos == "S":
            start = x

    if start is None:
        return False

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze [j][i] == "#"):
            return False
        
    return True

#function to find the end of the maze
def findEnd (maze, moves):
    start = None
    for x, pos in enumerate(maze[0]):
        if pos == "S":
            start = x
    if start is None:
        return False

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "G":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True
    
    return False


nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze()

while not findEnd(maze, add):
    if nums.empty():
        print("Can't find path.")
        break
    add = nums.get()

    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
