import can
import time

class CANInterface:
    def __init__(self,channel="vcan0",bitrate=500000):
        self.channel=channel
        self.bitrate=bitrate
        
        try:
            self.bus=can.interface.Bus(channel=self.channel,bustype="socketcan")
            print(f"[CAN] connected to {self.channel}")
        except Exception as e:
            print(f"[CAN ERROR] {e}")
            self.bus=None
            
    def send_message(self,arbitration_id,data):
        if self.bus is None:
            return
        message=can.Message(arbitration_id=arbitration_id, data=data,is_extended_id=False)
        try:
            self.bus.send(message)
            print(f"[TX] ID: {hex(arbitration_id)}  Data: {data}")
        except can.CanError:
            print("[ERROR] Message NOT sent")
            
    def receive_message(self,timeout=1.0):
        if self.bus is None:
            return
        try:
            message=self.bus.recv(timeout)
            return message
        except Exception as e:
            print(f"[RX ERROR] {e}")
            return None
