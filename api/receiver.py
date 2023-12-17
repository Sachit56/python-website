import socket
from threading import Thread
from taipy.gui import Gui, State, invoke_callback, get_state_id
import pandas as pd

HOST = "127.0.0.1"
PORT = 5050

state_id_list = []

def on_init(state: State):
    state_id = get_state_id(state)
    if (state_id := get_state_id(state)) is not None:
        state_id_list.append(state_id)
def client_handler(gui: Gui, state_id_list: list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, _ = s.accept()
    while True:
        if data := conn.recv(1024):
            print(f"Data received: {data.decode()}")
            if hasattr(gui, "_server") and state_id_list:
                invoke_callback(
                    gui, state_id_list[0], update_received_data, (str(data.decode()),)
                )
        else:
            print("Connection closed")
            break


def update_received_data(state: State, val):
    state.received_data = val
    temp_data=state.data
    temp_data["Price"][3]=state.received_data.split(",")[0]
    state.plot_location=state.received_data.split(",")[1]
    state.data=temp_data
received_data = 0
data = {
    "Date": pd.date_range("2023-04-12", periods=4, freq="D"),
    "Price": [2200000, 19700000, 270000, 6.5],
    
}

title = "Real State Simulator using python"
logo = "logo.jpeg"
plot_location = 'Bhaktapur'
plot_max_price = 500000000
plot_min_price = 100000000

def run(state):
    print(f'{plot_max_price} is maximum.')

    print(state.plot_location)

    with open("data.txt","a") as f:
        f.write(f'{state.plot_location} ,{state.plot_max_price} ,{state.plot_min_price}\n')

md = """
<| text-center
<|{logo}|image|>

<|{title}|>

Location of Plot:<|{plot_location}|input|>

Maximum Price:<|{plot_max_price}|number|>

Minimum Price:<|{plot_min_price}|number|>

<|Submit|button|on_action=run|>

<|{data}|chart|mode=lines|x=Date|y[1]=Price|line[1]=red|>

|>
Received Data:<|{received_data}|>
"""
gui = Gui(page=md)

t = Thread(
    target=client_handler,
    args=(
        gui,
        state_id_list,
    ),
)
t.start()

gui.run(title="Receiver Page")
