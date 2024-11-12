from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class BluetoothDevice(Base):
    __tablename__ = "bluetooth_devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)         # 블루투스 장치 이름
    mac_address = Column(String, unique=True) # 블루투스 장치의 MAC 주소
    is_connected = Column(Boolean, default=False)  # 연결 상태 여부