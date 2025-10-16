# Python 3.9 슬림 이미지를 베이스로 사용 (용량 최적화)
FROM python:3.9-slim

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

COPY requirements.txt .

# 필요한 Python 패키지 설치
# --no-cache-dir → pip 캐시를 저장하지 않아 이미지 크기 감소
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일을 컨테이너로 복사
COPY app.py .

# 컨테이너가 5000번 포트를 사용함을 명시 (문서화 목적)
EXPOSE 5000

# 컨테이너 실행 시 실행할 명령어
# python → Python 인터프리터 실행
# app.py → 실행할 파일
CMD ["python", "app.py"]
