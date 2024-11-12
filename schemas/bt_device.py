from pydantic import BaseModel

# 블루투스 장치 상태 응답 스키마
class BluetoothDeviceResponse(BaseModel):
    id: int
    name: str
    mac_address: str
    is_connected: bool

    class Config:
        from_attributes = True

# 블루투스 장치 연결 요청 스키마
class BluetoothDeviceConnectRequest(BaseModel):
    name: str         # 장치 이름
    mac_address: str  # 장치 MAC 주소

