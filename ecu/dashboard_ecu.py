import time
from common.can_interface import CANInterface

ENGINE_RPM_ID=0x100
BRAKE_ID=0x200

LOG_FILE="logs/can.log"

def log_message(message):
    with open(LOG_FILE,"a") as f:
        f.write(message + "\n")
        
def main():
    can_bus=CANInterface()
    
    current_rpm=0
    brake_status="Unknown"
    print("[Dashboard ECU] Started")
    
    while True:
        message=can_bus.receive_message(timeout=1.0)
        
        if message is None:
            continue
        timestamp =time.strftime("%Y-%m-%d %H:%M:%S")
        if message.arbitration_id == ENGINE_RPM_ID:
            current_rpm = int.from_bytes(message.data[0:2], byteorder='big')

        elif message.arbitration_id == BRAKE_ID:
            brake_status = "Pressed" if message.data[0] else "Released"

        output = f"[{timestamp}] RPM: {current_rpm} | Brake: {brake_status}"
        print(output)

        log_message(output)


if __name__ == "__main__":
    main()
