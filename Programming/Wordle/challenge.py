import random
import socket

wordlist = open("wordlist.filtered")
words = wordlist.read().split("\n")




def wordle_game(client: socket):
    client.send("Guess the words (5 attempts left)".encode())
    data = client.recv(1024).decode('utf-8').strip()
    word_index = random.randint(0, len(words) - 1)
    word = words[word_index]
    print(word)
    if not data:
        # Een error message
        return
    if data == word:
        client.send("Congrats you guessed the word!".encode())



host = "0.0.0.0"
port = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
while True:
    c, addr = server.accept()
    print('Connected to :', addr[0], ':', addr[1])
    thread = threading.Thread(target=wordle_game, args=(c,))
    thread.start()