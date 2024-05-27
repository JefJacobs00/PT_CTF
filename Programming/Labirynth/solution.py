import random
from pwn import *


#IP = "127.0.0.1"
IP = "108.143.241.81"
PORT = 1337

numbers = []
attempt = {}

def get_directions(connection):
    possible_directions = []
    recv = connection.recvuntil(b"Congrats", timeout=0.5).decode("utf-8")
    if "Congrats" in recv:
        print("Next layer found")
        return True
    recv = connection.recvuntil(b"?>", timeout=0.1).decode("utf-8")
    print(recv)
    directions = ["down", "up", "right", "left"]
    for direction in directions:
        if direction in recv:
            possible_directions.append(direction)

    return possible_directions


connection = remote(IP, PORT)
intro = connection.recvuntil(b"You can go ")
print(intro.decode('utf-8'))

def str_to_cord(str):
    y, x = str.split(',')
    return int(y), int(x)

def cord_to_str(cord):
    y, x = cord
    return f"{y},{x}"


def find_exit():
    position = (0, 0)
    graph = {}

    next_step(position, graph, 0)

def next_step(position, graph, n):
    if n == 5:
        return
    visited = []
    print(f"Entering layer:  {n}")
    move(visited, [], graph, position, None)
    next_step((0, 0), {}, n +1)

def calculate_direction(position, next_position):
    direction_changes = {"1,0": "up", "-1,0": "down", "0,1": "left", "0,-1": "right"}

    y, x = position
    next_y, next_x = next_position

    diff_cord = y - next_y, x - next_x
    diff_str = cord_to_str(diff_cord)
    return direction_changes[diff_str]


def move(visited, dead_end, graph, position, prev_pos):
    possible_directions = get_directions(connection)
    if type(possible_directions) == bool:
        return True
    add_directions_to_graph(possible_directions, position, graph)

    location = cord_to_str(position)
    visited.append(location)
    for node in graph[cord_to_str(position)]:
        # check if visited (being visited) or dead_end (finished visiting) --> move to edge if false
        if node not in visited and node not in dead_end:
            # calculate direction
            direction = calculate_direction(position, str_to_cord(node))
            connection.sendline(f"{direction}".encode('utf-8'))
            print(f"Moving to: {node}; by going {direction}")
            next_layer = move(visited, dead_end, graph, str_to_cord(node), position)
            if next_layer:
                return True


    dead_end.append(location)
    direction = calculate_direction(position, prev_pos)

    connection.sendline(f"{direction}".encode('utf-8'))
    print(f"Moving back to: {cord_to_str(prev_pos)}; by going {direction}")
    recv = connection.recvuntil(b"?>", timeout=0.1).decode("utf-8")
    print(recv)


def add_directions_to_graph(possible_directions, position, graph):
    direction_changes = {"down": (1, 0), "right": (0, 1), "up": (-1, 0), "left": (0, -1)}
    for direction in possible_directions:
        move_y, move_x = direction_changes[direction]
        y, x = position
        new_cord = (y + move_y, x + move_x)

        str = cord_to_str(new_cord)
        position_str = cord_to_str(position)

        if position_str not in graph:
            graph[position_str] = []
        if str not in graph:
            graph[str] = []

        if position_str not in graph[str]:
            graph[str].append(position_str)
        if str not in graph[position_str]:
            graph[position_str].append(str)



find_exit()
connection.interactive()
