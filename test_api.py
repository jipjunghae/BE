import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 1. GET /courses - 전체 강좌 목록 조회
def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert "data" in response.json()  # 응답에 'data' 키가 포함되어 있는지 확인

# 2. GET /courses/{course_id} - 특정 강좌 정보 조회
def test_get_course_info():
    course_id = 1  # 실제 테스트 데이터베이스에 있는 course_id로 설정해야 함
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert "courseName" in response.json()
    assert "professorName" in response.json()

# 3. GET /courses/{course_id}/lectures - 특정 강좌의 모든 강의 조회
def test_get_lectures_for_course():
    course_id = 1  # 실제 course_id로 설정
    response = client.get(f"/courses/{course_id}/lectures")
    assert response.status_code == 200
    assert "data" in response.json()

# 4. GET /courses/{course_id}/lectures/{lecture_id} - 특정 강의 정보 조회
def test_get_lecture_info():
    course_id = 1  # 실제 course_id로 설정
    lecture_id = 1  # 실제 lecture_id로 설정
    response = client.get(f"/courses/{course_id}/lectures/{lecture_id}")
    assert response.status_code == 200
    assert "lectureName" in response.json()
    assert "lectureLength" in response.json()
    assert "analysis" in response.json()

# 5. GET /courses/{course_id}/lectures/{lecture_id}/play - 특정 강의 비디오 재생
def test_play_lecture_video():
    course_id = 1  # 실제 course_id로 설정
    lecture_id = 1  # 실제 lecture_id로 설정
    response = client.get(f"/courses/{course_id}/lectures/{lecture_id}/play")
    assert response.status_code == 200
    assert response.headers["content-type"] == "video/mp4"

# 6. GET /notification-list - 읽지 않은 모든 알림 조회
def test_get_notifications():
    response = client.get("/notification-list")
    assert response.status_code == 200
    assert "data" in response.json()

# 7. POST /notification - 새로운 알림 추가
def test_add_notification():
    payload = {
        "message": "Test Notification",
        "is_read": False,
        "link": "/some/link"
    }
    response = client.post("/notification", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == payload["message"]
    assert response.json()["is_read"] == payload["is_read"]

# 8. GET /bt-linked - 블루투스 연결 여부 확인
def test_check_bt_connection():
    response = client.get("/bt-linked")
    assert response.status_code == 200
    assert "is_connected" in response.json()

# 9. POST /bt-linked/device - 블루투스 장치 연결
def test_connect_bt_device():
    payload = {
        "name": "Test Bluetooth Device",
        "mac_address": "00:1A:7D:DA:71:13"
    }
    response = client.post("/bt-linked/device", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]
    assert response.json()["is_connected"] is True

# 10. DELETE /bt-linked/device - 블루투스 장치 연결 해제
def test_disconnect_bt_device():
    mac_address = "00:1A:7D:DA:71:13"  # 실제 MAC 주소
    response = client.delete("/bt-linked/device", params={"mac_address": mac_address})
    assert response.status_code == 200
    assert response.json() == {"message": f"Device {mac_address} disconnected successfully"}
