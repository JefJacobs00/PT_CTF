# import socket programming library
import socket
import math
import random
import threading


VALUE = int(math.pow(10, 9))
GOAL = 10
seed = random.randint(1, VALUE)
banner = """
/$$$$$$            /$$$$$$  /$$           /$$   /$$                     /$$                     /$$      
|_  $$_/           /$$__  $$|__/          |__/  | $$                    | $$                    | $$      
  | $$   /$$$$$$$ | $$  \__/ /$$ /$$$$$$$  /$$ /$$$$$$    /$$$$$$       | $$ /$$   /$$  /$$$$$$$| $$   /$$
  | $$  | $$__  $$| $$$$    | $$| $$__  $$| $$|_  $$_/   /$$__  $$      | $$| $$  | $$ /$$_____/| $$  /$$/
  | $$  | $$  \ $$| $$_/    | $$| $$  \ $$| $$  | $$    | $$$$$$$$      | $$| $$  | $$| $$      | $$$$$$/ 
  | $$  | $$  | $$| $$      | $$| $$  | $$| $$  | $$ /$$| $$_____/      | $$| $$  | $$| $$      | $$_  $$ 
 /$$$$$$| $$  | $$| $$      | $$| $$  | $$| $$  |  $$$$/|  $$$$$$$      | $$|  $$$$$$/|  $$$$$$$| $$ \  $$
|______/|__/  |__/|__/      |__/|__/  |__/|__/   \___/   \_______/      |__/ \______/  \_______/|__/  \__/

Can you guess the random number between 1 and 10 a billion times? If you do i'll give you the flag.
Surely you would need infinite luck, or is it just a one in a billion chance?

Rules:
    Guess a value and go on to the next round, if you can gues the value a billion times you win!
    Easy, right? Good luck 🍀 (you will need it :D)
    

"""

def __print_rules(client_socket: socket):
    client_socket.send(banner.encode())
    client_socket.send("🍀> ".encode())

def __check_value( data):
    value = random.randint(1, 10)
    value = 1
    if not data.isnumeric():
        return "The character sent is not an integer."
    if value != int(data):
        return f"Sorry your value was wrong, better luck next time..."

    return "Nice, you go onto the next round!!"

def value_guesser(client_socket):
    __print_rules(client_socket)
    random.seed(seed)
    guessed = 0
    while guessed < GOAL:
        data = client_socket.recv(1024).decode('utf-8').strip()
        if data:
            print(data)
            answer = __check_value(data)
            client_socket.send(answer.encode())
            if "next round" in answer:
                client_socket.send("\n🍀> ".encode())
                guessed += 1
            else:
                print("Client closed")
                client_socket.close()
                return

    print("Client won")
    client_socket.close()


host = "192.168.0.186"
port = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
while True:
    c, addr = server.accept()
    print('Connected to :', addr[0], ':', addr[1])
    thread = threading.Thread(target = value_guesser, args = (c, ))
    thread.start()
server.close()


