from sqlalchemy.orm import Session
from models.bt_device import BluetoothDevice
from schemas.bt_device import BluetoothDeviceConnectRequest

# 현재 연결된 장치가 있는지 조회하는 함수
def get_connected_device(db: Session):
    return db.query(BluetoothDevice).filter(BluetoothDevice.is_connected == True).first()

# 블루투스 장치 연결 함수
def connect_bluetooth_device(db: Session, device_data: BluetoothDeviceConnectRequest):
    device = db.query(BluetoothDevice).filter_by(mac_address=device_data.mac_address).first()
    if not device:
        # 새 블루투스 장치 추가
        device = BluetoothDevice(name=device_data.name, mac_address=device_data.mac_address, is_connected=True)
        db.add(device)
    else:
        # 기존 장치를 연결 상태로 업데이트
        device.is_connected = True
    db.commit()
    db.refresh(device)
    return device

# 블루투스 장치 연결 해제 함수
def disconnect_bluetooth_device(db: Session, mac_address: str):
    device = db.query(BluetoothDevice).filter_by(mac_address=mac_address).first()
    if device:
        device.is_connected = False
        db.commit()
        db.refresh(device)
    return device
