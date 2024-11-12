from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.bt_device import BluetoothDeviceResponse, BluetoothDeviceConnectRequest
from services.bt_service import get_connected_device, connect_bluetooth_device, disconnect_bluetooth_device

router = APIRouter()

# 의존성 주입 - 데이터베이스 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 연결된 장치가 있는지 여부를 bool로 반환
@router.get("/bt-linked")
async def is_device_connected(db: Session = Depends(get_db)):
    connected_device = get_connected_device(db)
    return {"is_connected": bool(connected_device)}

# 특정 장치를 연결 (프론트엔드에서 장치를 선택하고 연결한 후 호출)
@router.post("/bt-linked/device", response_model=BluetoothDeviceResponse)
async def connect_device(device: BluetoothDeviceConnectRequest, db: Session = Depends(get_db)):
    connected_device = connect_bluetooth_device(db, device)
    return connected_device

# 현재 연결된 장치의 연결 해제
@router.delete("/bt-linked/device")
async def disconnect_device(db: Session = Depends(get_db)):
    connected_device = get_connected_device(db)
    if connected_device:
        disconnect_bluetooth_device(db, connected_device.mac_address)
        return {"message": "Device disconnected successfully"}
    else:
        raise HTTPException(status_code=404, detail="No device is currently connected")
