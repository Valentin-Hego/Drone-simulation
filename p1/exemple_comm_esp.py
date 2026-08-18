import serial
import time

port = serial.Serial('COM3', 115200, timeout=2)
time.sleep(2)  # Attendre le boot de l'ESP32
port.reset_input_buffer()

def read_usr():
    string = port.readline()
    return string.decode().strip()


def write_usr(cmd):
    port.write((cmd + '\n').encode())


while True:
    cmd = input()
    write_usr(cmd)

    string = read_usr()
    print(string)