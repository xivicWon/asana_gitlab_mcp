import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()
# 예시 토큰 및 URL (환경변수 또는 config 파일로 분리 권장)
ASANA_TOKEN = os.getenv("ASANA_TOKEN")
ASANA_BASE_URL = "https://app.asana.com/api/1.0"

GITLAB_TOKEN = os.getenv("GITLAB_ACCESS_TOKEN")
GITLAB_PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")
GITLAB_BASE_URL = "https://gitlab.your-company.com/api/v4"


def get_asana_issue(issue_id: str) -> Dict:
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    response = requests.get(f"{ASANA_BASE_URL}/tasks/{issue_id}", headers=headers)
    response.raise_for_status()
    return response.json()["data"]


def create_gitlab_issue(title: str, description: str) -> Dict:
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {
        "title": title,
        "description": description
    }
    response = requests.post(
        f"{GITLAB_BASE_URL}/projects/{GITLAB_PROJECT_ID}/issues",
        headers=headers,
        data=data
    )
    response.raise_for_status()
    return response.json()


def create_gitlab_branch(branch_name: str, ref: str = "main") -> Dict:
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {
        "branch": branch_name,
        "ref": ref
    }
    response = requests.post(
        f"{GITLAB_BASE_URL}/projects/{GITLAB_PROJECT_ID}/repository/branches",
        headers=headers,
        data=data
    )
    response.raise_for_status()
    return response.json()


def create_gitlab_merge_request(source_branch: str, target_branch: str, title: str, description: str) -> Dict:
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {
        "source_branch": source_branch,
        "target_branch": target_branch,
        "title": title,
        "description": description
    }
    response = requests.post(
        f"{GITLAB_BASE_URL}/projects/{GITLAB_PROJECT_ID}/merge_requests",
        headers=headers,
        data=data
    )
    response.raise_for_status()
    return response.json()


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("/", "-")[:40]


def trigger_mcp(asana_id: str):
    asana_issue = get_asana_issue(asana_id)
    title = asana_issue["name"]
    description = asana_issue.get("notes", "")
    short_title = slugify(title)
    branch_name = f"feature/asana-{asana_id}-{short_title}"
    print(f"[✔] Asana 이슈: {title} (ID: {asana_id})")
    print(f"[✔] 브랜치 이름: {branch_name}")
    print(f"[✔] 설명: {description}")
    
    print("[+] GitLab 이슈 생성 중...")
    gitlab_issue = create_gitlab_issue(title, description)

    print("[+] 브랜치 생성 중...")
    create_gitlab_branch(branch_name)

    print("[+] Merge Request 생성 중...")
    mr = create_gitlab_merge_request(
        source_branch=branch_name,
        target_branch="main",
        title=title,
        description=f"연동된 Asana ID: {asana_id}\n\n{description}"
    )
    print("[✔] 완료: MR URL:", mr.get("web_url"))


# 실행 예시
if __name__ == "__main__":
    trigger_mcp("your_asana_issue_id")
