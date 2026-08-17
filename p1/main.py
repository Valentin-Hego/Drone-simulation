import subprocess

def get_joystick():
    process = subprocess.Popen(
        ['python', '-u', 'joystick.py'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )
    
    try:
        for line in process.stdout:
            order = line.strip()
            print(f"Ordre reçu : {order}")
            
            
    except KeyboardInterrupt:
        process.terminate()

get_joystick()