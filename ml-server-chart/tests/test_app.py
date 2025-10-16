# pytest로 Flask 앱 테스트
import pytest
from app import app

# pytest fixture - 테스트용 클라이언트 생성
@pytest.fixture
def client():
    # 테스트 모드로 앱 설정
    app.config['TESTING'] = True
    # 테스트 클라이언트 생성
    with app.test_client() as client:
        yield client

# 루트 경로 테스트
def test_home(client):
    # GET 요청 전송
    response = client.get('/')
    # 상태 코드 확인
    assert response.status_code == 200
    # JSON 데이터 확인
    data = response.get_json()
    assert 'message' in data

# 헬스체크 테스트
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
