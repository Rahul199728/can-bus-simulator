import random
import time
from common.can_interface import CANInterface

BRAKE_ID = 0x200
    
def main():
    can_bus=CANInterface()
    print("[Brake ECU] Started")
    
    while True:
        brake_status=random.choice([0,1])

        # 8-byte CAN frame
        data = [brake_status,0, 0, 0, 0, 0, 0, 0]
        
        can_bus.send_message(BRAKE_ID, data)
        state= "Pressed" if brake_status else "Released"
        print(f"[BRAKE ECU] Brake: {state}")
        time.sleep(0.5) #every 500 ms
        
if __name__=="__main__":
    main()
