
import time
import socket

from random import randint

HOST = "127.0.0.1"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        with open("../data.txt", "r") as f:
            data = f.read()
        values = [val.strip() for val in data.split(",")]

        
        if len(values) == 3:
            name, max_val, min_val = values 
            print(name, min_val, max_val)

            
            try:
                random_number1 = randint(int(min_val), int(max_val))
                print(f"Generated random number: {random_number1} {name}")
                s.sendall(f"{random_number1},{name}".encode())
            except ValueError as e:
                print(f"Error converting to integers: {e}")
        else:
            print("Error: Unexpected format in data.txt")

        time.sleep(2)
