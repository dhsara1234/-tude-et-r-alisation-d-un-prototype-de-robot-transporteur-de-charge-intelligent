from socket import *
import Modules.KeyboardModule as kp
from Modules.utils import s

# from main import motor

socket = socket()
HOST = "192.168.137.46"
PORT = 9999
ADDRESS = (HOST, PORT)
BUF_SIZE = 1024
socket.bind(ADDRESS)
socket.listen(5)
# connect to the server on local computer
con, addr = socket.accept()
last_position = 324
while True:
    initial = 0
    stations = {initial: last_position, 1: 290, 2: 290, 3: 300, 4: 300, 5: 300, 6: 300}
    data = con.recv(1024).decode()
    try:
        som = s(stations, int(data), initial)
        if som > last_position:
            print(f"Going forward for {som - last_position}cm")
            #     motor.move(0.6, 0, (som - last_position) / 0.6)
            last_position = som
        else:
            print(f"Going backward for {som - last_position}cm")
            #     motor.move(-0.6, 0, (som - last_position) / 0.6)
            last_position = som
    except Exception:
        # if kp.getKey(data):
        #     motor.move(0.6, 0, 0.1)
        # elif kp.getKey(data):
        #     motor.move(-0.6, 0, 0.1)
        # elif kp.getKey(data):
        #     motor.move(0.5, 0.3, 0.1)
        # elif kp.getKey(data):
        #     motor.move(0.5, -0.3, 0.1)
        # else:
        #     motor.stop(0.1)
        print(data)
        continue
