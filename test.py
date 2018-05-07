# 모듈 임포트
from flask import Flask
app = Flask(__name__)


# /기본 라우트와 요청 핸들러 정의
@app.route("/")
def hello():
	return "Hello, Python!!"


# 실행된 파일이 main 프로그램인지 확인하고 앱 실행	
if __name__ == "__main__":
	app.run()