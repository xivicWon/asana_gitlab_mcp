# 실행 환경 설정

```sh
# common
pip install -r requirements.txt


# for mac
python3 -m venv venv
source venv/bin/activate


# for window
python -m venv venv
.\venv\Scripts\Activate.ps1
```

# 실행 방법

```sh
uvicorn mcp_server:app --reload
# or for mac
python3 mcp_server.py

# or for window
python mcp_server.py
```

# API 테스트 방법

```sh
# 서버가 acitvate 및 uvicorn 으로 app을 활성화 시킨 뒤에 아래 curl 을 호출.
curl -X POST "http://127.0.0.1:8000/mcp/trigger" -H "Content-Type: application/json" -d "{\"asana_issue_id\": \"1210494780822950\"}"
```

# 종료 방법

```sh
deactivate
```

# 성공한 멘트

- 아사나 이슈 1210494780822946 에 대해 gitlab 브랜치를 생성해줘
