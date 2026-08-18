import subprocess
import serial
import time

port = serial.Serial('COM3', 115200, timeout=2)
time.sleep(2)  # Attendre le boot de l'ESP32
port.reset_input_buffer()

def write_usr(cmd):
    port.write((cmd + '\n').encode())

def get_joystick():
    process = subprocess.Popen(
        ['python', '-u', 'joystick.py'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )
    
    try:
        # on print l'ordre une seul fois jusqu'a ce qu'il change
        prev_order = ""
        for line in process.stdout:
            order = line.strip()

            if (order == "TIR") :
                print(f"Ordre reçu : {order}")
                write_usr(order)
                prev_order = order

            elif (order != prev_order) :
                print(f"Ordre reçu : {order}")
                write_usr(order)
                prev_order = order

    except KeyboardInterrupt:
        process.terminate()

get_joystick()