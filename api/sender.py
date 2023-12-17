import time
import socket

from random import randint

HOST = "127.0.0.1"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        with open("../data.txt","r") as f:
            data=f.read()
        # name, max, min =data.split(",")
        print(data)

     
        random_number1 = randint(int(1), int(100))
        s.sendall(f"{random_number1},".encode())
        print(f"Sending: {random_number1}")
        time.sleep(2)
