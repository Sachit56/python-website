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
        values = [val.strip() for val in data.split(",")]

        # Check if the split produced at least three values
        if len(values) >= 3:
            name, max_val, min_val = values[:3]  # Take the first three values
            print(name, min_val, max_val)

     
        random_number1 = randint(int(min_val), int(max_val))
        s.sendall(f"{random_number1},{name}".encode())
        print(f"Sending: {random_number1}{name}")
        time.sleep(2)
