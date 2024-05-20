import random


def number_to_cord(number, row_size):
    return (number // row_size, number % row_size)

def cord_to_number(cord, row_size):
    y, x = cord
    number = x
    number += y * row_size

    return number

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
    def mst_to_graph(self, mst):
        graph = {}
        for i in range(1, len(mst)):
            node_to = mst[i]
            if i not in graph:
                graph[i] = []
            if node_to not in graph:
                graph[node_to] = []

            graph[i].append(node_to)
            graph[node_to].append(i)

        self.graph = graph

    def _min_key(self, key, mst_set):
        min_val = float('inf')
        min_idx = -1

        for v in range(self.n * self.n):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_idx = v

        return min_idx

def print_possible_paths(position, graph, row_size):
    paths = []
    y, x = position
    position_index = cord_to_number(position, row_size)
    edges = graph[position_index]
    for edge in edges:
        y_edge, x_edge = number_to_cord(edge, row_size)
        if y != y_edge:
            if y > y_edge:
                paths.append("u")
                print('You can go up')
            else:
                paths.append("d")
                print('You can go down')
        elif x != x_edge:
            if x > x_edge:
                paths.append("l")
                print('You can go left')
            else:
                paths.append("r")
                print("You can go right")
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

I will let you know what paths are viable, you don't have to stick to the paths, 
Keep in mind that you are not yet a ghost, so you might want to avoid running into a wall.
"""
print(intro)

layers = [3, 5, 10, 20, 50, 100]
for n in layers:
    graph = Graph(n)
    mst = graph.prim_mst()
    graph.mst_to_graph(mst)
    finish_coord = (n - 1, n - 1)

    #col, row
    position = (0,0)
    previous_position = (0, 0)

    while True:
        paths = print_possible_paths(position, graph.graph, n)
        direction = input("\nWhere do you want to go?\n?> ")

        try:

            position = move(direction[0], position, paths)
            previous_position = position
            if position == finish_coord:
                print("Congrats you found the entrance to the next floor")
                break
        except Exception as e:
            print(e)
            exit()

        print(position)



