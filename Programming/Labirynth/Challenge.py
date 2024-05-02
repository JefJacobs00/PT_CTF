import random

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {}
        self.construct_graph()

    def construct_graph(self):
        for i in range(1, self.n * self.n + 1):
            self.graph[i] = {}
            row = (i - 1) // self.n
            col = (i - 1) % self.n
            if row > 0:  # Connect to node above
                self.graph[i][i - self.n] = random.randint(1, 10)  # Random weight
            if row < self.n - 1:  # Connect to node below
                self.graph[i][i + self.n] = random.randint(1, 10)  # Random weight
            if col > 0:  # Connect to node left
                self.graph[i][i - 1] = random.randint(1, 10)  # Random weight
            if col < self.n - 1:  # Connect to node right
                self.graph[i][i + 1] = random.randint(1, 10)  # Random weight

    def prim_mst(self):
        mst = [None] * (self.n * self.n)
        key = [float('inf')] * (self.n * self.n)
        mst_set = [False] * (self.n * self.n)

        key[0] = 0
        mst[0] = -1

        for _ in range(self.n * self.n - 1):
            u = self._min_key(key, mst_set)
            mst_set[u] = True

            for v in self.graph[u + 1]:
                if not mst_set[v - 1] and 1 <= u + 1 < self.n * self.n and 1 <= v <= self.n * self.n:
                    if key[v - 1] > self.graph[u + 1][v]:  # Check if current weight is smaller
                        mst[v - 1] = u
                        key[v - 1] = self.graph[u + 1][v]

        return mst

    def _min_key(self, key, mst_set):
        min_val = float('inf')
        min_idx = -1

        for v in range(self.n * self.n):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_idx = v

        return min_idx

def visualize(mst, n):
    layout = []
    layout.append(["S"])
    for i in range(1, len(mst)):
        source = (i//n, i%n)
        dest = (mst[i]//n, mst[i]%n)
        if source[1] == 0:
            layout.append([])
        # columns
        if dest[1] != source[1]:
            layout[source[0]].append("H")
        # rows
        elif dest[0] != source[0]:
            layout[source[0]].append("V")

    return layout


def print_possible_paths(position, layout, max):
    paths = ["b"]
    y, x = position
    if y - 1 >= 0 and (layout[y - 1][x] == "V" or layout[y - 1][x] == "S"):
        print("You can go up.")
        paths.append("u")
    if y + 1 < max and (layout[y + 1][x] == "V" or layout[y + 1][x] == "S"):
        print("You can go down.")
        paths.append("d")
    if x - 1 >= 0 and (layout[y][x - 1] == "H" or layout[y][x - 1] == "S"):
        print("You can go left.")
        paths.append("l")
    if x + 1 < max and (layout[y][x + 1] == "H" or layout[y][x + 1] == "S"):
        print("You can go right.")
        paths.append("r")

    return paths

death_message = ["""
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░       ░▒▓██████▓▒░   ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 
 
""","""
 ▄▀▀▀▀▄    ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█         ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐     █      █ █   █    █ ▐  ▄▀   ▐ █   █   █ 
█    ▀▄▄    █▄▄▄█ ▐  █    █   █▄▄▄▄▄      █      █ ▐  █    █    █▄▄▄▄▄  ▐  █▀▀█▀  
█     █ █  ▄▀   █   █    █    █    ▌      ▀▄    ▄▀    █   ▄▀    █    ▌   ▄▀    █  
▐▀▄▄▄▄▀ ▐ █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄         ▀▀▀▀       ▀▄▀     ▄▀▄▄▄▄   █     █   
▐         ▐   ▐   █    █     █    ▐                            █    ▐   ▐     ▐   
                  ▐    ▐     ▐                                 ▐                  
""",
"""
  ______ _______ _______ _______       _____  _    _ _______  ______
 |  ____ |_____| |  |  | |______      |     |  \  /  |______ |_____/
 |_____| |     | |  |  | |______      |_____|   \/   |______ |    \_                                                               
""",
"""
     _        _        _        _        _        _        _        _        _    
   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__ 
 _|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|
(_ G _ (_(_ A _ (_(_ M _ (_(_ E _ (_(_   _ (_(_ O _ (_(_ V _ (_(_ E _ (_(_ R _ (_ 
  |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__|
""",
"""
██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝                                                         
"""]

def move(move_direction, current_position, possible_paths):
    if move_direction not in possible_paths:
        c = random.randint(0, len(death_message))
        raise Exception(death_message[c])
    y, x = current_position
    match move_direction:
        case "u":
            return y - 1, x
        case "d":
            return y + 1, x
        case "l":
            return y, x - 1
        case "r":
            return y, x + 1


intro = r"""
  _           _                _       _   _     
 | |         | |              (_)     | | | |    
 | |     __ _| |__  _   _ _ __ _ _ __ | |_| |__  
 | |    / _` | '_ \| | | | '__| | '_ \| __| '_ \ 
 | |___| (_| | |_) | |_| | |  | | | | | |_| | | |
 |______\__,_|_.__/ \__, |_|  |_|_| |_|\__|_| |_|
                     __/ |                       
                    |___/                        

You have entered the labyrinth. There are multiple floors and you need to find the exit. 
Be careful you have a limited amount of time before the labyrinth changes.

Wandering for to long on a single floor can also trigger some evil spirits that will haunt you 👻.
You can move through the labyrinth by typing if you want to go: 

u: up
d: down
l: left
r: right 

you can always go back by entering b.

I will let you know what paths are viable, you don't have to stick to the paths, 
Keep in mind that you are not yet a ghost, so you might want to avoid running into a wall.
"""
print(intro)

layers = [3, 5, 10, 20, 50, 100]
for n in layers:
    graph = Graph(n)
    mst = graph.prim_mst()
    print(mst)
    layout = visualize(mst, n)
    finish_index = random.randint(1, len(mst))
    finish_coord = (finish_index // n, finish_index % n)
    print(finish_coord)
    print(layout)

    #col, row
    position = (0,0)
    previous_position = (0, 0)

    while True:
        paths = print_possible_paths(position, layout, n)
        direction = input("\nWhere do you want to go?\n?> ")

        try:
            if direction == "b":
                position = previous_position
            else:
                position = move(direction[0], position, paths)
            previous_position = position
            if position == finish_coord:
                print("Congrats you found the entrance to the next floor")
                break
        except Exception as e:
            print(e)
            exit()

        print(position)



