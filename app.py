# Flask 웹 프레임워크 import
from flask import Flask, jsonify
# 운영체제 정보를 가져오기 위한 모듈
import socket

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

# 루트 경로(/) 요청 처리
@app.route('/')
def home():
    return jsonify({
        "message": "Hello from ML Model Server!",
        "hostname": socket.gethostname()  # Pod 이름 확인용
    })

# 헬스체크 엔드포인트 - Kubernetes liveness/readiness probe용
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# 메트릭 엔드포인트 - 모니터링용
@app.route('/metrics')
def metrics():
    return jsonify({
        "requests_total": 100,
        "requests_success": 95,
        "requests_failed": 5
    })

# 애플리케이션 실행
# host='0.0.0.0' → 모든 네트워크 인터페이스에서 접근 가능
# port=5000 → 5000번 포트에서 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
