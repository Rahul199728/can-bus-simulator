import random
import time
from common.can_interface import CANInterface

ENGINE_RPM_ID = 0x100

def generate_rpm():
    return random.randint(800,4000)
    
def main():
    can_bus=CANInterface()
    print("[Engine ECU] Started")
    
    while True:
        rpm=generate_rpm()
        # Convert RPM to 2 bytes
        rpm_bytes = rpm.to_bytes(2, byteorder='big')

        # 8-byte CAN frame
        data = [rpm_bytes[0], rpm_bytes[1], 0, 0, 0, 0, 0, 0]
        
        can_bus.send_message(ENGINE_RPM_ID, data)
        print(f"[Engine ECU] RPM Sent: {rpm}")
        time.sleep(0.1) #every 100 ms
        
if __name__=="__main__":
    main()
