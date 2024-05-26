# import socket programming library
import socket
import math
import random
import threading

VALUE = int(math.pow(10, 6))
GOAL = 1000
seed = random.randint(1, VALUE)
banner = r"""
/$$$$$$            /$$$$$$  /$$           /$$   /$$                     /$$                     /$$      
|_  $$_/           /$$__  $$|__/          |__/  | $$                    | $$                    | $$      
  | $$   /$$$$$$$ | $$  \__/ /$$ /$$$$$$$  /$$ /$$$$$$    /$$$$$$       | $$ /$$   /$$  /$$$$$$$| $$   /$$
  | $$  | $$__  $$| $$$$    | $$| $$__  $$| $$|_  $$_/   /$$__  $$      | $$| $$  | $$ /$$_____/| $$  /$$/
  | $$  | $$  \ $$| $$_/    | $$| $$  \ $$| $$  | $$    | $$$$$$$$      | $$| $$  | $$| $$      | $$$$$$/ 
  | $$  | $$  | $$| $$      | $$| $$  | $$| $$  | $$ /$$| $$_____/      | $$| $$  | $$| $$      | $$_  $$ 
 /$$$$$$| $$  | $$| $$      | $$| $$  | $$| $$  |  $$$$/|  $$$$$$$      | $$|  $$$$$$/|  $$$$$$$| $$ \  $$
|______/|__/  |__/|__/      |__/|__/  |__/|__/   \___/   \_______/      |__/ \______/  \_______/|__/  \__/

Can you guess the random number between 1 and 10 a thousand times? If you do i'll give you the flag.
Surely you would need infinite luck, or is it just a one in a thousand chance?

Rules:
    Guess a value and go on to the next round, if you can gues the value a billion times you win!
    Easy, right? Good luck 🍀 (you will need it :D). 

    (There will be a surprise at the end)


"""


def __print_rules(client_socket: socket):
    client_socket.send(banner.encode())
    client_socket.send("🍀> ".encode())


def __check_value(data):
    value = random.randint(1, 10)

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
            answer = __check_value(data)
            client_socket.send(answer.encode())
            if "next round" in answer:
                client_socket.send("\n🍀> ".encode())
                guessed += 1
            else:
                print("Client closed")
                client_socket.close()
                return

    #client_socket.send("You won, here is your flag! If you can tell me what the randomly generated seed was...\n #> ".encode())
    #data = client_socket.recv(1024).decode("utf-8").strip()
    client_socket.send("flag: ctf{flag}".encode())
    #if data == f"{seed}":
        #client_socket.send("flag: ctf{s33ds_4r3_us3l3ss!}".encode())
    #else:
        #print(f"{data} =? {seed}")
        #client_socket.send("That was not the seed, better luck next time")

    client_socket.close()


host = "0.0.0.0"
port = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
while True:
    c, addr = server.accept()
    print('Connected to :', addr[0], ':', addr[1])
    thread = threading.Thread(target=value_guesser, args=(c,))
    thread.start()
server.close()


